class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # val:index

        for index, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return (index, seen[diff])
            seen[num] = index
        return
