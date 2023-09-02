class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP (top down)
        # O(n * amount) time complexity
        # O(n * amount) space for tabulation
        n = len(coins)
        dp = [[0 for _ in range(amount + 1)] for _ in range(n + 1)]
        for j in range(1, amount + 1):
            dp[0][j] = float("inf")
        
        for i in range(1, n + 1):
            for j in range(amount + 1):
                if coins[i - 1] <= j:
                    dp[i][j] = \
                        min(1 + dp[i][j - coins[i - 1]], dp[i - 1][j])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount] if dp[n][amount] != float("inf") else -1