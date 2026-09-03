from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litters = []
        start = None
        
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))
                    
        k = len(litters)
        target_mask = (1 << k) - 1
        
        if target_mask == 0:
            return 0
            
        litter_map = {pos: i for i, pos in enumerate(litters)}
        
        # Queue stores: (r, c, current_energy, mask, moves)
        queue = deque([(start[0], start[1], energy, 0, 0)])
        # Visited dict mapping (r, c, mask) -> max_energy
        visited = {(start[0], start[1], 0): energy}
        
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, curr_e, mask, moves = queue.popleft()
            
            if mask == target_mask:
                return moves
                
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or classroom[nr][nc] == 'X':
                    continue
                    
                # Moving costs 1 energy unit
                next_e = curr_e - 1
                if next_e < 0:
                    continue
                    
                next_mask = mask
                cell = classroom[nr][nc]
                
                # Recharge happens AFTER successfully stepping into the 'R' cell
                if cell == 'R':
                    next_e = energy
                elif cell == 'L':
                    idx = litter_map[(nr, nc)]
                    next_mask |= (1 << idx)
                    
                if next_mask == target_mask:
                    return moves + 1
                    
                state_key = (nr, nc, next_mask)
                if next_e > visited.get(state_key, -1):
                    visited[state_key] = next_e
                    queue.append((nr, nc, next_e, next_mask, moves + 1))
                    
        return -1
