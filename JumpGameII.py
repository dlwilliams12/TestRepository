from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach, n = 0, len(nums)
        count = 1
        for i, jump in enumerate(nums):
            max_reach = max(max_reach, i + jump)
            if max_reach <= i:
                count -= 1
                return count
            if max_reach == 0:
                max_reach = max(max_reach, i + jump - 1)
            
            if max_reach >= n -1:
                return count
            
            count += 1
                