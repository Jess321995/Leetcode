class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Recursive
        @cache
        def countSubset(n, sum):
            if(n == 0 and sum > 0):
                return 0
            if(sum==0 and n==0):
                return 1
        
            if(n>0 and sum>=0):
                if nums[n - 1] <= sum:
                    return (countSubset(n - 1,  sum - nums[n - 1]) + \
                            countSubset(n - 1,  sum))
                else:
                    return countSubset(n - 1,  sum)
        
        sum = 0
        for n in nums:
            sum += n

        if (sum - target) % 2 != 0 or sum < target:
            return 0
        val = (sum - target) // 2
        return countSubset(len(nums), val)
