class LazySegmentTree:
    def __init__(self, n, MOD=10**9 + 7):
        self.n = n
        self.MOD = MOD
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.sum_sq = [0] * (4 * n)

    def _push(self, node, start, end):
        if self.lazy[node] != 0:
            val = self.lazy[node]
            mid = (start + end) // 2
            
            # Left child update
            left_node = 2 * node
            self.sum_sq[left_node] = (self.sum_sq[left_node] + 2 * val * self.tree[left_node] + val * val * (mid - start + 1)) % self.MOD
            self.tree[left_node] = (self.tree[left_node] + val * (mid - start + 1)) % self.MOD
            self.lazy[left_node] = (self.lazy[left_node] + val) % self.MOD
            
            # Right child update
            right_node = 2 * node + 1
            self.sum_sq[right_node] = (self.sum_sq[right_node] + 2 * val * self.tree[right_node] + val * val * (end - mid)) % self.MOD
            self.tree[right_node] = (self.tree[right_node] + val * (end - mid)) % self.MOD
            self.lazy[right_node] = (self.lazy[right_node] + val) % self.MOD
            
            self.lazy[node] = 0

    def update_range(self, l, r, node, start, end, val):
        if r < start or end < l:
            return
        if l <= start and end <= r:
            self.sum_sq[node] = (self.sum_sq[node] + 2 * val * self.tree[node] + val * val * (end - start + 1)) % self.MOD
            self.tree[node] = (self.tree[node] + val * (end - start + 1)) % self.MOD
            self.lazy[node] = (self.lazy[node] + val) % self.MOD
            return
        
        self._push(node, start, end)
        mid = (start + end) // 2
        self.update_range(l, r, 2 * node, start, mid, val)
        self.update_range(l, r, 2 * node + 1, mid + 1, end, val)
        
        # Correctly merge values from children back into the parent node
        self.sum_sq[node] = (self.sum_sq[2 * node] + self.sum_sq[2 * node + 1]) % self.MOD
        self.tree[node] = (self.tree[2 * node] + self.tree[2 * node + 1]) % self.MOD


class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        seg = LazySegmentTree(n, MOD)
        last_seen = {}
        ans = 0

        for r in range(n):
            l = last_seen.get(nums[r], -1) + 1
            seg.update_range(l, r, 1, 0, n - 1, 1)
            last_seen[nums[r]] = r
            
            # The root node (index 1) always tracks the current total sum of squares
            ans = (ans + seg.sum_sq[1]) % MOD

        return ans
