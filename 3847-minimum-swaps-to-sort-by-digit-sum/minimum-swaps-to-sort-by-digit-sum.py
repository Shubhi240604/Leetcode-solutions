class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n: int) -> int:
            return sum(int(d) for d in str(n))
        
        n = len(nums)
        
       
        sorted_arr = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        
        
        target_idx = {val: i for i, val in enumerate(sorted_arr)}
        
        visited = [False] * n
        total_cycles = 0
        
       
        for i in range(n):
            if visited[i]:
                continue
                
            total_cycles += 1
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = target_idx[nums[curr]]
                
        return n - total_cycles