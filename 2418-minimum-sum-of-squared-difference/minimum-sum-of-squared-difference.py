class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        
        
        k = k1 + k2
        if sum(diffs) <= k:
            return 0
            
        
        max_diff = max(diffs)
        count = [0] * (max_diff + 1)
        for d in diffs:
            count[d] += 1
            
        
        for d in range(max_diff, 0, -1):
            if count[d] == 0:
                continue
                
            
            ops_needed = count[d]
            
            if k >= ops_needed:
                k -= ops_needed
                count[d - 1] += count[d]
                count[d] = 0
            else:
                
                count[d - 1] += k
                count[d] -= k
                k = 0
                break
                
        
        return sum(freq * (d ** 2) for d, freq in enumerate(count))

