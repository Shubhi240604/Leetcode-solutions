class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        layer = 0
        for i in range(len(s) - 1):
            if s[i] == '(' and s[i+1] == ')':
                ans += 1 << layer
            layer += 1 if s[i] == '(' else -1
        return ans
