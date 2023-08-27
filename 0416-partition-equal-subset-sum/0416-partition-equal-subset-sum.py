class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Optimized DP solution
        # O(sum * n) time
        # O(sum) space
        def subset_problem(n, target_sum):
            dp = [False for _ in range(target_sum + 1)]
            dp[0] = True
            for i in range(1, n + 1):
                curRow = [False for _ in range(target_sum + 1)]
                curRow[0] = True
                for j in range(1, target_sum + 1):
                    if nums[i - 1] <= j:
                        curRow[j] = dp[j - nums[i-1]] or dp[j]
                    else:
                        curRow[j] = dp[j]
                dp = curRow
            
            return dp[target_sum]
        
        n = len(nums)
        sum = 0
        for val in nums:
            sum += val
        if sum % 2 != 0:
            return False
        else:
            return subset_problem(n, sum // 2)