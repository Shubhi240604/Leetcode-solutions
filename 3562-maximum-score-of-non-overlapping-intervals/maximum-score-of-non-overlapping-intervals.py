from functools import cache
import bisect

class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        # Attach original indices and sort by end time, then start time, then weight
        indexed_intervals = []
        for idx, (l, r, w) in enumerate(intervals):
            indexed_intervals.append((l, r, w, idx))
        
        indexed_intervals.sort(key=lambda x: (x[1], x[0], -x[2]))
        n = len(indexed_intervals)
        
        # Precompute the last non-overlapping interval index for each interval using binary search
        ends = [x[1] for x in indexed_intervals]
        prev_idx = []
        for i in range(n):
            l = indexed_intervals[i][0]
            # Find rightmost interval whose end time < l
            idx_found = bisect.bisect_left(ends, l) - 1
            prev_idx.append(idx_found)
            
        @cache
        def dp(i: int, k: int) -> tuple[int, list[int]]:
            if i < 0 or k == 0:
                return 0, []
            
            # Option 1: Skip current interval i
            skip_weight, skip_indices = dp(i - 1, k)
            
            # Option 2: Take current interval i
            p = prev_idx[i]
            prev_weight, prev_indices = dp(p, k - 1)
            take_weight = indexed_intervals[i][2] + prev_weight
            take_indices = sorted(prev_indices + [indexed_intervals[i][3]])
            
            # Compare options (maximize weight, tie-break with lexicographically smaller indices)
            if take_weight > skip_weight:
                return take_weight, take_indices
            elif take_weight < skip_weight:
                return skip_weight, skip_indices
            else:
                return take_weight, min(take_indices, skip_indices)

        return dp(n - 1, 4)[1]
