from typing import List

class Solution:
    def __init__(self, nums: List[int], target: int):
        self.my_list = nums
        self.my_target = target
    
    def twoSum(self) -> List[int]:
        n = len(self.my_list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if self.my_list[i] + self.my_list[j] == self.my_target:
                    return [i, j]
        return []  # No solution found
    
summe = Solution([2,7,11,15], 9)
print(summe.twoSum())

#[Approach - Brute Force, Complexity - , Runtime - ]