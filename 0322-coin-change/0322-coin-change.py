class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Memoization without cache decorator
        # O(n * amount) time complexity
        # O(n * amount) recursive stack space
        def helper(n, amount):
            if amount == 0:
                return 0
            if n == 0:
                return float("inf")
            
            if cache[n][amount] != -1:
                return cache[n][amount]

            if coins[n - 1] <= amount:
                cache[n][amount] = \
                    min(1 + helper(n, amount - coins[n - 1]),
                        helper(n - 1, amount))
            else:
                cache[n][amount] = helper(n - 1, amount)
            return cache[n][amount]

        n = len(coins)
        cache = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        val = helper(n, amount)
        return val if val != float("inf") else -1