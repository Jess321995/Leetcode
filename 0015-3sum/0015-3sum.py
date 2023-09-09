class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            # To avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # Use two pointers - one at start and other at end
            # to find the two elements in the remainder of the
            # sorted array
            l = i + 1
            r = len(nums) - 1
            while l < r:
                val = nums[i] + nums[l] + nums[r]
                if val > 0:
                    r -= 1
                elif val < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res