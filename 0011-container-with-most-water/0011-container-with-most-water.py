class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            length = min(height[r], height[l])
            breadth = r - l
            area = length * breadth
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea