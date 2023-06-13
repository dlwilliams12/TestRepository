from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        sume = 0
        keep_going = True
        while keep_going:
            sume = nums[i] + nums[j]
            if sume == target:
                return[i,j]
        