class Solution:
    
    def superEggDrop(self, k: int, n: int) -> int:
        cache = [[-1 for _ in range(n + 1)] for _ in range(k + 1)]
        
        def helper(k, n):
            if n == 0 or n == 1:
                return n
        
            if k == 1:
                return n

            if cache[k][n] != -1:
                return cache[k][n]

            minAttempts = n + 1
            low = 1
            high = n
            while low <= high:
                middle = (low + high) // 2
                # Made an attempt hence 1
                # Outcome could be either break or no break
                # and we take max of that since we need worst case
                left = helper(k - 1, middle - 1)
                right = helper(k, n - middle)
                temp = 1 + max(left, right)
                minAttempts = min(minAttempts, temp)
                if left < right:
                    low = middle + 1
                else:
                    high = middle - 1
            cache[k][n] = minAttempts
            return minAttempts

        return helper(k, n)