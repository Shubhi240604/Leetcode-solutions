class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        lookup = [0] * n
        stack = []
        
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                lookup[i] = j
                lookup[j] = i
                
        
        result = []
        curr_idx = 0
        direction = 1 
        
        while curr_idx < n:
            if s[curr_idx] == '(' or s[curr_idx] == ')':
                
                curr_idx = lookup[curr_idx]
                
                direction = -direction
            else:
                
                result.append(s[curr_idx])
            
            
            curr_idx += direction
            
        return "".join(result)
