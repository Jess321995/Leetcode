class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(n, cur):
            if n == 0:
                res.append(cur.copy())
                return
            cur.append(nums[n - 1])
            helper(n - 1, cur)
            cur.pop()
            while n >= 2 and nums[n - 2] == nums[n - 1]:
                n = n - 1
            helper(n - 1, cur)

        helper(len(nums), [])
        return res