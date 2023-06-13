from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        k = 0
        # Increment the length of the list, removing any number in the list 
        # thats equal t val. Return length of list.
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)
nums = [3,2,2,3]
val = 3
# Create an instance of Solution and call removeElement method.
sol = Solution()
k = sol.removeElement(nums, val)
expectedNums = [2,2]
assert k == len(expectedNums)
# Sort and print list
nums.sort()
print("Modified nums list:", end=' ')
for num in nums:
    print(num, end=' ')
    