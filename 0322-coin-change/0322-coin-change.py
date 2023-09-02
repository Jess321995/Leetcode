class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Memoization
        @cache
        def helper(n, amount):
            if amount == 0:
                return 0
            if n == 0:
                return float("inf")

            if coins[n - 1] <= amount:
                return min(1 + helper(n, amount - coins[n - 1]), helper(n - 1, amount))
            else:
                return helper(n - 1, amount)
        
        #cache = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]

        val = helper(len(coins), amount)
        return val if val != float("inf") else -1