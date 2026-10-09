class Solution:
    def minInsertions(self, s: str) -> int:
        neededRight = 0
        ans = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                if neededRight % 2 != 0:
                    ans += 1
                    neededRight -= 1
                neededRight += 2
            else:
                neededRight -= 1
                if neededRight < 0:
                    ans += 1
                    neededRight += 2
            i += 1
            
        return ans + neededRight
