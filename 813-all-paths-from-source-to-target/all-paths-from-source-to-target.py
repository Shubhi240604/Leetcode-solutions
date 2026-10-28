class Solution:
    def allPathsSourceTarget(self, graph):
        target = len(graph) - 1
        results = []
        
        def dfs(node, current_path):
            if node == target:
                results.append(list(current_path))
                return
            
            for neighbor in graph[node]:
                current_path.append(neighbor)
                dfs(neighbor, current_path)
                current_path.pop()
        
        dfs(0, [0])
        return results
