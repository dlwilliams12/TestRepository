from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return len(nums)
    
    # Previous Code
    
    #class Solution:
    # def removeDuplicates(self, nums: List[int]) -> int:
        
        #Type Error - range functions takes ints as arguments
        #not list.
    #     for i in range(nums): 
    #---------------------------------------------------------------
    #   #Error - deleting items in a list while iterating can cause issues
        #after index of elements change.
    #         if nums[i] == nums[i+1]:
    #             del nums[i+1]
    
        #Error - for loops iterates i, dont need to do it inside
        #the loop.
    #             i += 1
    #         else:
    #             i += 1
                
    #     return len(nums)