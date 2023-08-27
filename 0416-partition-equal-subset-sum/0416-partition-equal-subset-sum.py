class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # DP solution
        def subset_problem(n, target_sum):
            for i in range(1, n + 1):
                for j in range(1, target_sum + 1):
                    if nums[i - 1] <= j:
                        cache[i][j] = \
                            (cache[i-1][j - nums[i-1]] or cache[i-1][j])
                    else:
                        cache[i][j] = cache[i-1][j]
            
            return cache[n][target_sum]
        
        n = len(nums)
        sum = 0
        for val in nums:
            sum += val
        cache = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            cache[i][0] = True

        if sum % 2 != 0:
            return False
        else:
            return subset_problem(n, sum // 2)