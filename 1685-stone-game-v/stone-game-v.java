import java.util.Arrays;

class Solution {
    private int[][] memo;
    private int[] prefixSum;

    public int stoneGameV(int[] stoneValue) {
        int n = stoneValue.length;
        memo = new int[n][n];
        for (int[] row : memo) {
            Arrays.fill(row, -1);
        }

        prefixSum = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixSum[i + 1] = prefixSum[i] + stoneValue[i];
        }

        return dp(0, n - 1, stoneValue);
    }

    private int dp(int l, int r, int[] stoneValue) {
        if (l == r) {
            return 0;
        }
        if (memo[l][r] != -1) {
            return memo[l][r];
        }

        int maxScore = 0;
        for (int k = l; k < r; k++) {
            int leftSum = prefixSum[k + 1] - prefixSum[l];
            int rightSum = prefixSum[r + 1] - prefixSum[k + 1];

            if (leftSum < rightSum) {
                maxScore = Math.max(maxScore, leftSum + dp(l, k, stoneValue));
            } else if (leftSum > rightSum) {
                maxScore = Math.max(maxScore, rightSum + dp(k + 1, r, stoneValue));
            } else {
                maxScore = Math.max(maxScore, leftSum + Math.max(dp(l, k, stoneValue), dp(k + 1, r, stoneValue)));
            }
        }

        return memo[l][r] = maxScore;
    }
}
