class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        output = []
        def helper(n, target, res):
            print(res)
            # Found the answer
            if target == 0 and len(res) == k:
                output.append(res.copy())
                return
            if target <= 0:
                return
            if len(res) > k:
                return
            if n == 0:
                return

            # Choose it
            res.append(n - 1)
            helper(n - 1, target - n + 1, res)
            # Don't choose it
            res.pop()
            helper(n - 1, target, res)

        helper(10, n, [])
        return output 