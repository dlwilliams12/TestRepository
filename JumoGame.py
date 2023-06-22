from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, n = 0, len(nums)
        for i, jump in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= n - 1:
                return True
            max_reach = max(max_reach, i + jump)
        return False















#[Old Code] from typing import List

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         jump = False
#         i = 0
#         while i < len(nums) and nums[i] != 0:
#             for i in range(len(nums)):
#                 if len(nums) -1 - nums[i] == 1:
#                     jump = True
                            
#         return jump
    