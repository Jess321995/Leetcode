class Solution:
    def shortestCommonSupersequence(self, text1: str, text2: str) -> str:
        # DP
        # O(i*j) time complexity
        # O(i*j) space complexity
        dp = [[0 for _ in range(len(text2) + 1)]
                 for _ in range(len(text1) + 1)]
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):   
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) 
        
        i, j = len(text1), len(text2)
        res = ""
        while i > 0 and j > 0:
            if text1[i - 1] == text2[j - 1]:
                res += text1[i - 1]
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    res += text1[i - 1]
                    i -= 1
                else:
                    res += text2[j - 1]
                    j -= 1
        while i > 0:
            res += text1[i - 1]
            i -= 1
        while j > 0:
            res += text2[j - 1]
            j -= 1
        return res[::-1]