class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        # If it's impossible to reach the sum with 'num' digits
        if num * 9 < sum:
            return ""
        
        # Greedily take as many 9s as possible
        k, s = divmod(sum, 9)
        ans = "9" * k
        
        # Append the remainder if there is one
        if s:
            ans += str(s)
            
        # Pad with trailing zeros to match the required 'num' digits
        ans += "0" * (num - len(ans))
        
        return ans
