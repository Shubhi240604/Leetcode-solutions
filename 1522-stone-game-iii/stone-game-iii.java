class Solution {
    public String stoneGameIII(int[] stoneValue) {
        int n = stoneValue.length;
        
        int[] dp = new int[4];
        int sum = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            sum += stoneValue[i];
            int bestValue = Integer.MIN_VALUE;
            
            int currentSum = 0;
            for (int k = 1; k <= 3 && i + k - 1 < n; k++) {
                currentSum += stoneValue[i + k - 1];
                bestValue = Math.max(bestValue, currentSum - dp[(i + k) % 4]);
            }
            dp[i % 4] = bestValue;
        }
        
        if (dp[0 % 4] > 0) {
            return "Alice";
        } else if (dp[0 % 4] < 0) {
            return "Bob";
        } else {
            return "Tie";
        }
    }
}
