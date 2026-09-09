class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        
        def dfs(node, target):
            if not node:
                return
            
            path.append(node.val)
            
            # Check if it's a leaf node and sums up to target
            if not node.left and not node.right and target == node.val:
                result.append(list(path))
            else:
                dfs(node.left, target - node.val)
                dfs(node.right, target - node.val)
                
            path.pop() # Backtrack
            
        dfs(root, targetSum)
        return result
