class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bits[i] += 1
        
        mod = 10**9 + 7
        ans = 0
        
        for _ in range(k):
            curr = 0
            for i in range(32):
                if bits[i] > 0:
                    curr |= (1 << i)
                    bits[i] -= 1
            ans = (ans + curr * curr) % mod
            
        return ans
