from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        i = 0
        my_map = {}
        for i in nums:
            if i in my_map:
                my_map[i] += 1
            else:
                my_map[i] = 1
        max_key = max(my_map, key = my_map.get)
        return max_key
            
solution = Solution()
nums = [2,2,1,1,1,2,2]
majority = solution.majorityElement(nums)

print(f"The majority element is {majority}")