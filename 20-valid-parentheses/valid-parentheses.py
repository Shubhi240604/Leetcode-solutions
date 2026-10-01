class Solution:
    def isValid(self, s: str) -> bool:
        
        close_to_open = {")": "(", "}": "{", "]": "["}
        stack = []

        for char in s:
            
            if char in close_to_open:
                
                top_element = stack.pop() if stack else '#'
                
               
                if close_to_open[char] != top_element:
                    return False
            else:
                
                stack.append(char)

        
        return not stack
