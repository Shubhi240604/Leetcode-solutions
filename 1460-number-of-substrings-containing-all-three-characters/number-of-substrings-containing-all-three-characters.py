class Solution:

  def numberOfSubstrings(self, s: str) -> int:
    ans = l = 0
    cnt = {
        'a': 0,
        'b': 0,
        'c': 0,
    }  
    for r, c in enumerate(s):
      cnt[c] += 1
     
      while cnt['a'] > 0 and cnt['b'] > 0 and cnt['c'] > 0:
        cnt[s[l]] -= 1
        l += 1
      
      ans += l

    return ans
