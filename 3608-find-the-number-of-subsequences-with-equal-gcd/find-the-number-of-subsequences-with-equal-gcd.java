import java.util.Arrays;

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[][][] memo;

    public int subsequencePairCount(int[] nums) {
        int n = nums.length;
        int maxVal = 0;
        for (int num : nums) {
            maxVal = Math.max(maxVal, num);
        }

        
        memo = new int[n][maxVal + 1][maxVal + 1];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= maxVal; j++) {
                Arrays.fill(memo[i][j], -1);
            }
        }

        
        return solve(0, 0, 0, nums, maxVal);
    }

    private int solve(int idx, int gcd1, int gcd2, int[] nums, int maxVal) {
        
        if (idx == nums.length) {
            
            if (gcd1 > 0 && gcd1 == gcd2) {
                return 1;
            }
            return 0;
        }

       
        if (memo[idx][gcd1][gcd2] != -1) {
            return memo[idx][gcd1][gcd2];
        }

        
        long ans = solve(idx + 1, gcd1, gcd2, nums, maxVal);

        
        int nextGcd1 = (gcd1 == 0) ? nums[idx] : gcd(gcd1, nums[idx]);
        ans = (ans + solve(idx + 1, nextGcd1, gcd2, nums, maxVal)) % MOD;

        
        int nextGcd2 = (gcd2 == 0) ? nums[idx] : gcd(gcd2, nums[idx]);
        ans = (ans + solve(idx + 1, gcd1, nextGcd2, nums, maxVal)) % MOD;

        return memo[idx][gcd1][gcd2] = (int) ans;
    }


    private int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}
