class Solution:
    def mergeAdjacent(self, nums: list[int]) -> list[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            while len(stack) > 1 and stack[-1] == stack[-2]:
                last = stack.pop()
                second_last = stack.pop()
                stack.append(last + second_last)
                
        return stack
