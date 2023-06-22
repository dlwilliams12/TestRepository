from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jump = False
        i = 0
        while nums[i] != 0:
            