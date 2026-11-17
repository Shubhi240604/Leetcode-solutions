import itertools

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        factors = self._getFactors(n)
        
        cost = self._getCost(s, n, factors)
        
       
        dp = [[n] * (k + 1) for _ in range(n + 1)]
        dp[n][0] = 0
        
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                
                for l in range(i + 1, n):
                    dp[i][j] = min(dp[i][j], dp[l + 1][j - 1] + cost[i][l])
                    
        return dp[0][k]

    def _getFactors(self, n: int) -> list[list[int]]:
        factors = [[1] for _ in range(n + 1)]
        for d in range(2, n):
            for i in range(d * 2, n + 1, d):
                factors[i].append(d)
        return factors

    def _getCost(self, s: str, n: int, factors: list[list[int]]) -> list[list[int]]:
        cost = [[n] * n for _ in range(n)]
        for i, j in itertools.combinations(range(n), 2):
            length = j - i + 1
            min_changes = length
            for d in factors[length]:
                changes = 0
                
                for offset in range(d):
                    left = i + offset
                    right = j - d + 1 + offset
                    while left < right:
                        if s[left] != s[right]:
                            changes += 1
                        left += d
                        right -= d
                min_changes = min(min_changes, changes)
            cost[i][j] = min_changes
        return cost
