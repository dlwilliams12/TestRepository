from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        max_reach, steps, count = nums[0], nums[0], 1
        for i in range(1, n):
            if i > steps:
                count += 1
                steps = max_reach
            max_reach = max(max_reach, i + nums[i])
        return count    
                
solution = Solution()
nums = [1,2,1,1,1]
result = solution.jump(nums)
print(result)