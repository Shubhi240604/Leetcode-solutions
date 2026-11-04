import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        
        
        small = []  
        large = []  
        
        small_size = 0
        large_size = 0
        small_sum = 0
        large_sum = 0
        
        del_small = {}
        del_large = {}
        
        def prune(heap, del_dict):
            while heap and del_dict.get(heap[0], 0) > 0:
                val = heapq.heappop(heap)
                del_dict[val] -= 1
                
        
        cost = [0] * (n - x + 1)
        
        for i in range(n):
            val = nums[i]
            
            if not small or val <= -small[0]:
                heapq.heappush(small, -val)
                small_size += 1
                small_sum += val
            else:
                heapq.heappush(large, val)
                large_size += 1
                large_sum += val
                
           
            if i >= x:
                out = nums[i - x]
                if small and out <= -small[0]:
                    del_small[-out] = del_small.get(-out, 0) + 1
                    small_size -= 1
                    small_sum -= out
                else:
                    del_large[out] = del_large.get(out, 0) + 1
                    large_size -= 1
                    large_sum -= out
            
            
            while small_size < large_size:
                prune(large, del_large)
                moved = heapq.heappop(large)
                large_size -= 1
                large_sum -= moved
                heapq.heappush(small, -moved)
                small_size += 1
                small_sum += moved
                
            while small_size > large_size + 1:
                prune(small, del_small)
                moved = -heapq.heappop(small)
                small_size -= 1
                small_sum -= moved
                heapq.heappush(large, moved)
                large_size += 1
                large_sum += moved
                
            prune(small, del_small)
            prune(large, del_large)
            
            
            if i >= x - 1:
                median = -small[0]
                
                w_cost = (median * small_size - small_sum) + (large_sum - median * large_size)
                cost[i - x + 1] = w_cost

        
        INF = float('inf')
        dp = [0] + [INF] * k
        
       
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                
                dp[i][j] = dp[i - 1][j]
                
               
                if i >= x:
                    window_start_idx = i - x
                    if dp[window_start_idx][j - 1] != INF:
                        dp[i][j] = min(dp[i][j], dp[window_start_idx][j - 1] + cost[window_start_idx])
                        
        return dp[n][k]
