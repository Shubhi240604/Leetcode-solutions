class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 1_000_000_007
        import math
        # Choose 2*k points from n + k - 1 points
        return math.comb(n + k - 1, 2 * k) % MOD
