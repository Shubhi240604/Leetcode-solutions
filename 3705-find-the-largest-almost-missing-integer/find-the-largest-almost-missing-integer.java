import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int largestInteger(int[] nums, int k) {
        int n = nums.length;

        
        if (k == n) {
            int maxVal = -1;
            for (int num : nums) {
                maxVal = Math.max(maxVal, num);
            }
            return maxVal;
        }

        
        if (k == 1) {
            Map<Integer, Integer> countMap = new HashMap<>();
            for (int num : nums) {
                countMap.put(num, countMap.getOrDefault(num, 0) + 1);
            }
            int maxVal = -1;
            for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
                if (entry.getValue() == 1) {
                    maxVal = Math.max(maxVal, entry.getKey());
                }
            }
            return maxVal;
        }

       
        int firstElement = nums[0];
        int lastElement = nums[n - 1];
        
        int firstCount = 0;
        int lastCount = 0;
        
        for (int num : nums) {
            if (num == firstElement) firstCount++;
            if (num == lastElement) lastCount++;
        }

        int result = -1;
        
        if (firstCount == 1) {
            result = Math.max(result, firstElement);
        }
        
        if (lastCount == 1) {
            result = Math.max(result, lastElement);
        }

        return result;
    }
}
