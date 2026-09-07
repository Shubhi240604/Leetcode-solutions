class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        # dp stores the number of distinct subsequences ending with each character 'a'-'z'
        dp = [0] * 26
        
        for char in s:
            # The index for the current character (0 to 25)
            idx = ord(char) - ord('a')
            
            # The new count for subsequences ending in 'char' is equal to 
            # (all existing subsequences + 1 for the single character itself)
            dp[idx] = (sum(dp) + 1) % MOD
            
        # The total number of non-empty distinct subsequences is the sum of all ending counts
        return sum(dp) % MOD
