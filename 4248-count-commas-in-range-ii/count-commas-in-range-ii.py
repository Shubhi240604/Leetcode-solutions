class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        p = 1000
        while p <= n:
            total_commas += n - p + 1
            p *= 1000
        return total_commas
