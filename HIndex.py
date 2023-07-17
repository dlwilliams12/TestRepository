from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)
        new_list = []
        current_max = 0
        
        for i, cite in enumerate(citations):
            if n-1 == 0:
                return cite
            if cite / n <= cite:
                new_list.insert(i, cite)
                current_max = max(new_list)
                n -= i
        return current_max
            
solution = Solution()
nums = [3,0,6,1,5]
print(solution.hIndex(nums))