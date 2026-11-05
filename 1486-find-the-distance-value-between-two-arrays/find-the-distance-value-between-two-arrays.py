from typing import List
from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        arr2.sort()
        distance_value = 0
        
        for x in arr1:
            
            idx = bisect_left(arr2, x - d)
            
            
            if idx == len(arr2) or arr2[idx] > x + d:
                distance_value += 1
                
        return distance_value
