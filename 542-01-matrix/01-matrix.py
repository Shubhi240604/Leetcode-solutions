from collections import deque

class Solution(object):
    def updateMatrix(self, mat):
        if not mat or not mat[0]:
            return mat
            
        rows = len(mat)
        cols = len(mat[0])
        queue = deque()
        
        
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1  
                    
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                   
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))
                    
        return mat
