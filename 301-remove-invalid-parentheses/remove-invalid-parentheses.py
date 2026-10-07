class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
       
        left_rm = 0
        right_rm = 0
        for char in s:
            if char == '(':
                left_rm += 1
            elif char == ')':
                if left_rm > 0:
                    left_rm -= 1
                else:
                    right_rm += 1

        res = set()

        def dfs(index, left_count, right_count, left_rem, right_rem, curr_str):
            
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    res.add(curr_str)
                return

            char = s[index]

            
            if char == '(' and left_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem - 1, right_rem, curr_str)
            if char == ')' and right_rem > 0:
                dfs(index + 1, left_count, right_count, left_rem, right_rem - 1, curr_str)

           
            if char != '(' and char != ')':
                dfs(index + 1, left_count, right_count, left_rem, right_rem, curr_str + char)
            elif char == '(':
                dfs(index + 1, left_count + 1, right_count, left_rem, right_rem, curr_str + char)
            elif char == ')' and left_count > right_count:
                dfs(index + 1, left_count, right_count + 1, left_rem, right_rem, curr_str + char)

        dfs(0, 0, 0, left_rm, right_rm, "")
        return list(res)
