class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time complexity: O(2 ^ (t)) where t is the target 
        # Space complexity: Recursive stack space O(2 ^ (t)) + O(t) to store res
        output = []
        def helper(n, target, res):
            # Found the answer
            if target == 0:
                output.append(res.copy())
                return
            # Traversed entire array and no items left
            if n == 0:
                return

            # Value can be chosen
            if candidates[n - 1] <= target:
                # Choose it
                res.append(candidates[n - 1])
                helper(n, target - candidates[n - 1], res)
                # Don't choose it
                res.pop()
                helper(n - 1, target, res)

            # Value cannot be chosen
            else:
                helper(n - 1, target, res)

        helper(len(candidates), target, [])
        return output