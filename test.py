from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            index = abs(num) - 1  # Fix incorrect index reference
            if nums[index] < 0:
                result.append(index + 1)
            nums[index] = -nums[index]  # Negate value at index

        return result  # Fix incorrect return variable name

nums = [4, 3, 2, 7, 8, 2, 3, 1]
 
solution = Solution()  # Correct instance creation
print(solution.findDuplicates(nums))  # Correct method call