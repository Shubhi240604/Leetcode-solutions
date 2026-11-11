class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        cost_only_singles = need1 * cost1 + need2 * cost2
        
       
        cost_only_bundles = costBoth * max(need1, need2)
        
        
        mn = min(need1, need2)
        cost_mixed = costBoth * mn + (need1 - mn) * cost1 + (need2 - mn) * cost2
        
        return min(cost_only_singles, cost_only_bundles, cost_mixed)
