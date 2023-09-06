class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        if len(s1) <= 1:
            return False
        if len(s2) <= 1:
            return False
        
        n = len(s1)
        for i in range(1, n):
            # Swap
            cond1 = self.isScramble(s1[:i], s2[n - i: n]) and \
                self.isScramble(s1[i: n], s2[:n - i])
            # Don't swap
            cond2 = self.isScramble(s1[:i], s2[:i]) and \
                self.isScramble(s1[i: n], s2[i: n])
            if cond1 or cond2:
                return True
        return False