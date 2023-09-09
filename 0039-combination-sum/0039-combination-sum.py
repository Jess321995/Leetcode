class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        def helper(n, target, res):
            if target == 0:
                output.append(res.copy())
                return
            if n == 0:
                return

            # Choose the value
            if candidates[n - 1] <= target:
                res.append(candidates[n - 1])
                helper(n, target - candidates[n - 1], res)
                res.pop()
                helper(n - 1, target, res)
            else:
                helper(n - 1, target, res)

        helper(len(candidates), target, [])
        return output