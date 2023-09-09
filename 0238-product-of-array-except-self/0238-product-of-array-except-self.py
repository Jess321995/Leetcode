class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(n) time
        # O(n) space
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            postfix[len(nums) - 1 - i] = postfix[len(nums) - i] * nums[len(nums) - i]
        for i in range(len(nums)):
            nums[i] = prefix[i] * postfix[i]
        return nums
