class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Memoization solution
        def subset_problem(n, target_sum):
            if target_sum == 0:
                return True
            if n == 0:
                return False
            if cache[n][target_sum] != -1:
                return cache[n][target_sum]
            if nums[n - 1] <= target_sum:
                cache[n][target_sum] = \
                (subset_problem(n - 1, target_sum - nums[n- 1]) or
                 subset_problem(n - 1, target_sum))
            else:
                cache[n][target_sum] = subset_problem(n - 1, target_sum)
            
            return cache[n][target_sum]
        
        n = len(nums)
        sum = 0
        for val in nums:
            sum += val
        cache = [[-1 for _ in range(sum + 1)] for _ in range(n + 1)]
        if sum % 2 != 0:
            return False
        else:
            return subset_problem(n, sum // 2)