class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        queue = deque([root])
        is_even_level = True
        
        while queue:
            level_size = len(queue)
            prev_val = float('-inf') if is_even_level else float('inf')
            
            for _ in range(level_size):
                node = queue.popleft()
                val = node.val
                
                if is_even_level:
                    
                    if val % 2 == 0 or val <= prev_val:
                        return False
                else:
                    
                    if val % 2 != 0 or val >= prev_val:
                        return False
                
                prev_val = val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            is_even_level = not is_even_level
            
        return True
