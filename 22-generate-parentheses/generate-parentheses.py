class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(open_count, close_count, current_string):
            if open_count == n and close_count == n:
                res.append(current_string)
                return
            
            if open_count < n:
                backtrack(open_count + 1, close_count, current_string + '(')
                
            if close_count < open_count:
                backtrack(open_count, close_count + 1, current_string + ')')
                
        backtrack(0, 0, "")
        return res
