import java.util.Arrays;

class Solution {
    public int minimumPushes(String word) {
        
        int[] frequency = new int[26];
        for (char c : word.toCharArray()) {
            frequency[c - 'a']++;
        }
        
       
        Arrays.sort(frequency);
        
        int totalPushes = 0;
        
        
        for (int i = 0; i < 26; i++) {
            
            int currentFreq = frequency[26 - i - 1];
            
            
            if (currentFreq == 0) {
                break;
            }
            
            
            int pushesPerLetter = (i / 8) + 1;
            totalPushes += currentFreq * pushesPerLetter;
        }
        
        return totalPushes;
    }
}
