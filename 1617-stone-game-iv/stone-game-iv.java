class Solution {
    private Boolean[] memo;

    public boolean winnerSquareGame(int n) {
        memo = new Boolean[n + 1];
        return dfs(n);
    }

    private boolean dfs(int stones) {
        
        if (stones == 0) return false;
        
        
        if (memo[stones] != null) return memo[stones];

        
        for (int k = 1; k * k <= stones; k++) {
            
            if (!dfs(stones - k * k)) {
                return memo[stones] = true;
            }
        }

        
        return memo[stones] = false;
    }
}
