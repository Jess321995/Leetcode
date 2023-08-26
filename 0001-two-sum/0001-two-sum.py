class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #val:index
        map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in map:
                index = map[diff]
                return [index, i]
            else:
                map[n] = i