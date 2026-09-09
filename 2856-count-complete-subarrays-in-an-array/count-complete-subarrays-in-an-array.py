from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        # Step 1: Find the total number of distinct elements in the entire array
        target_distinct = len(set(nums))
        
        # Step 2: Initialize sliding window variables
        window_counts = Counter()
        left = 0
        total_subarrays = 0
        n = len(nums)
        
        # Step 3: Expand the window with the right pointer
        for right in range(n):
            window_counts[nums[right]] += 1
            
            # Shrink the window from the left as long as it contains all distinct elements
            while len(window_counts) == target_distinct:
                # If the current window from `left` to `right` is valid,
                # then any subarray starting at `left` and ending anywhere 
                # from `right` to the end of the array is also valid.
                total_subarrays += (n - right)
                
                # Remove the element at the left pointer and move it forward
                window_counts[nums[left]] -= 1
                if window_counts[nums[left]] == 0:
                    del window_counts[nums[left]]
                left += 1
                
        return total_subarrays
