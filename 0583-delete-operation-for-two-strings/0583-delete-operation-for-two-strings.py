class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        # DP
        # O(i*j) time complexity
        # O(j) space complexity
        dp = [0 for _ in range(len(text2) + 1)]
        for i in range(1, len(text1) + 1):
            curRow = [0 for _ in range(len(text2) + 1)]
            for j in range(1, len(text2) + 1):   
                if text1[i - 1] == text2[j - 1]:
                    curRow[j] = 1 + dp[j - 1]
                else:
                    curRow[j] = max(dp[j], curRow[j - 1]) 
            dp = curRow
        lcs = dp[len(text2)]
        return (len(text1) - lcs) + (len(text2) - lcs)