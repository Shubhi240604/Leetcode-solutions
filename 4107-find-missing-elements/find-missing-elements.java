import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public List<Integer> findMissingElements(int[] nums) {
        List<Integer> missingElements = new ArrayList<>();
        Set<Integer> presentNumbers = new HashSet<>();
        
        int minElement = Integer.MAX_VALUE;
        int maxElement = Integer.MIN_VALUE;
        
        
        for (int num : nums) {
            presentNumbers.add(num);
            if (num < minElement) {
                minElement = num;
            }
            if (num > maxElement) {
                maxElement = num;
            }
        }
        
        
        for (int current = minElement; current <= maxElement; current++) {
            if (!presentNumbers.contains(current)) {
                missingElements.add(current);
            }
        }
        
        return missingElements;
    }
}
