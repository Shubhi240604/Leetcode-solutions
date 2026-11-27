from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        
        dp = [0] * (budget + 1)
        min_price = float('inf')
        
        for factor, price in items:
            min_price = min(min_price, price)
            
            
            count = sum(1 for j_factor, _ in items if j_factor % factor == 0)
            
           
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)
                
        
        ans = 0
        for i in range(budget + 1):
            extra_items = (budget - i) // min_price
            ans = max(ans, dp[i] + extra_items)
            
        return ans
