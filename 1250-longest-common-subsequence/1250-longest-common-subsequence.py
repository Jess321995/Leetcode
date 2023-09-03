class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Memoization
        # O(i*j) time complexity
        # O(i*j) + O(i + j) = cache + recursive stack space complexity
        def lcs(i, j):
            if i == 0 or j == 0:
                return 0
            if cache[i][j] != -1:
                return cache[i][j]
            if text1[i - 1] == text2[j - 1]:
                cache[i][j] = 1 + lcs(i - 1, j - 1)
            else:
                cache[i][j] = max(lcs(i - 1, j), lcs(i, j - 1)) 
            return cache[i][j]

        cache = [[-1 for _ in range(len(text2) + 1)]
                 for _ in range(len(text1) + 1)]

        return lcs(len(text1), len(text2))