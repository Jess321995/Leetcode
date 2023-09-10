class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
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
                helper(n - 1, target - candidates[n - 1], res)
                # Don't choose it
                res.pop()
                # And don't choose any other value too that is a duplicate
                while n >= 2 and candidates[n - 2] == candidates[n - 1]:
                    n -= 1
                if n > 0:
                    helper(n - 1, target, res)

            # Value cannot be chosen
            else:
                # And don't choose any other value too that is a duplicate
                while n >= 2 and candidates[n - 2] == candidates[n - 1]:
                    n -= 1
                if n > 0:
                    helper(n - 1, target, res)

        helper(len(candidates), target, [])
        return output