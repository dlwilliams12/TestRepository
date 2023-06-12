from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            nums1[:] = sorted(nums1[:m] + nums2[:n])
            
# Create List of m,n integers
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

# Create object of solution class
s1 = Solution()

# Use merge method
s1.merge(nums1, m , nums2, n)

# Print result
print(nums1)