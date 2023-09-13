class Solution:
    def combinationSum4(self, candidates: List[int], target: int) -> int:
        n = len(candidates)
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for j in range(1, target + 1):
            for n in candidates:
                dp[j] += dp[j - n] if (j - n) >= 0 else 0
        return dp[target] 
             
        #Recursive
        #output = 0
        #def helper(goal):
        #    nonlocal output
        #    # Found the answer
        #    if goal == 0:
        #        output += 1
        #        return

        #    if goal < 0:
        #        return
            
        #    for n in candidates:
        #        helper(goal - n)

        #helper(target)
        #return output