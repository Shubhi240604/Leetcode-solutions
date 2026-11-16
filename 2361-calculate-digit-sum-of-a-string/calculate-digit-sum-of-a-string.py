class Solution:
  def digitSum(self, s: str, k: int) -> str:
    while len(s) > k:
      next_groups = []
      for i in range(0, len(s), k):
        summ = sum(int(s[j]) for j in range(i, min(len(s), i + k)))
        next_groups.append(str(summ))
      s = ''.join(next_groups)
    return s
