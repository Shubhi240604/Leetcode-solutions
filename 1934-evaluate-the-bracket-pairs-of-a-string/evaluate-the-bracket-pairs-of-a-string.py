
class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        # Convert knowledge array to a dictionary for O(1) lookups
        d = {key: value for key, value in knowledge}
        
        i, n = 0, len(s)
        ans = []
        
        while i < n:
            if s[i] == '(':
                # Find the closing bracket position
                j = s.find(')', i + 1)
                # Extract key, lookup in dictionary, default to '?' if missing
                key = s[i + 1:j]
                ans.append(d.get(key, '?'))
                i = j + 1
            else:
                ans.append(s[i])
                i += 1
                
        return ''.join(ans)
