class Solution:
    def minCost(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        
        dp = [[set() for _ in range(n)] for _ in range(m)]
        
        
        dp[0][0].add(grid[0][0])
        
        for r in range(m):
            for c in range(n):
                
                if r == 0 and c == 0:
                    continue
                    
                val = grid[r][c]
                
                
                if r > 0:
                    for prev_xor in dp[r - 1][c]:
                        dp[r][c].add(prev_xor ^ val)
                        
                
                if c > 0:
                    for prev_xor in dp[r][c - 1]:
                        dp[r][c].add(prev_xor ^ val)
                        
        
        return min(dp[m - 1][n - 1])
