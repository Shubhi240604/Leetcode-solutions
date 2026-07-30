class Solution {
    public int minimumPushes(String word) {
        int ans = 0;
        int n = word.length();
        
        // Distribute characters across 8 keys (2-9)
        for (int i = 0; i < n; i++) {
            ans += (i / 8) + 1;
        }
        
        return ans;
    }
}
