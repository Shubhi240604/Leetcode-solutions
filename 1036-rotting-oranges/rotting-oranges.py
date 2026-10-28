from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        if not grid:
            return 0
            
        rows, cols = len(grid), len(grid[0]) # Fixed a minor bug here too: len(grid[0]) for cols
        queue = deque()
        fresh_count = 0
        minutes = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_count += 1
                    
        if fresh_count == 0:
            return 0
            
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue and fresh_count > 0:
            minutes += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append((nr, nc))
                        
        return minutes if fresh_count == 0 else -1
