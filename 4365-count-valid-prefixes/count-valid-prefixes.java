class Solution {
    public int countValidPrefixes(String s) {
        int validCount = 0;
        int count0 = 0;
        int count1 = 0;
        
        
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '0') {
                count0++;
            } else {
                count1++;
            }
            
            
            if (Math.abs(count0 - count1) <= 1) {
                validCount++;
            }
        }
        
        return validCount;
    }
}
