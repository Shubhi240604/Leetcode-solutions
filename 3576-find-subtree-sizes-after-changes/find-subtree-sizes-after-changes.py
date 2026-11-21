from collections import defaultdict
from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[parent[i]].append(i)
            
        ans = [0] * n
        
        ancestors = defaultdict(list)
        
        def dfs(u: int, p: int) -> None:
            ans[u] = 1
            char = s[u]
            ancestors[char].append(u)
            
            
            for v in tree[u]:
                dfs(v, u)
                
            
            target_parent = p
            if len(ancestors[char]) > 1:
               
                target_parent = ancestors[char][-2]
                
            
            if target_parent != -1:
                ans[target_parent] += ans[u]
                
            
            ancestors[char].pop()
            
        dfs(0, -1)
        return ans
