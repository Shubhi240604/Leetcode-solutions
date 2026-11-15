from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        even_count = 1 
        odd_count = 0
        prefix_sum = 0
        total = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 1:
                total = (total + even_count) % MOD
                odd_count += 1
            else:
                total = (total + odd_count) % MOD
                even_count += 1

        return total
