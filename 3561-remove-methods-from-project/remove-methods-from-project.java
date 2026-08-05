class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        List<List<Integer>> graph = new ArrayList<>();
        List<Integer> allMethods = new ArrayList<>();
        
        for (int i = 0; i < n; i++) {
            allMethods.add(i);
            graph.add(new ArrayList<>());
        }
        
        for (int[] inv : invocations) {
            graph.get(inv[0]).add(inv[1]);
        }
        
        
        boolean[] isSuspicious = new boolean[n];
        dfs(k, graph, isSuspicious);
        
        
        for (int i = 0; i < n; i++) {
            if (!isSuspicious[i]) {
                for (int next : graph.get(i)) {
                    if (isSuspicious[next]) {
                        
                        return allMethods;
                    }
                }
            }
        }
        
        
        List<Integer> remaining = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!isSuspicious[i]) {
                remaining.add(i);
            }
        }
        
        return remaining;
    }
    
    private void dfs(int node, List<List<Integer>> graph, boolean[] isSuspicious) {
        isSuspicious[node] = true;
        for (int next : graph.get(node)) {
            if (!isSuspicious[next]) {
                dfs(next, graph, isSuspicious);
            }
        }
    }
}

