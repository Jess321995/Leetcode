class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total_sum = sum(nums)

        # Check if it's possible to achieve the target sum based on the total sum
        if (total_sum - target) % 2 != 0 or total_sum < target:
            return 0

        subset_sum = (total_sum - target) // 2

        # Create a DP matrix with dimensions (len(nums) + 1) x (subset_sum + 1)
        dp = [[0] * (subset_sum + 1) for _ in range(len(nums) + 1)]

        # There's one way to achieve a sum of 0 (by not selecting any number)
        dp[0][0] = 1

        # Fill in the DP matrix
        for i in range(1, len(nums) + 1):
            for j in range(subset_sum + 1):
                dp[i][j] = dp[i - 1][j]  # Exclude the current number
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # Include the current number

        return dp[len(nums)][subset_sum]
        

