class Solution:
    def climbStairs(self, n: int) -> int:
        # dynamic programming
        one, two = 0,1
        for i in range(n):
            tmp = one + two
            one = two
            two = tmp
        return two