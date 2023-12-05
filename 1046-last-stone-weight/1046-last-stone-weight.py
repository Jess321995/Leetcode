class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first, second = heapq.heappop(stones), heapq.heappop(stones)
            heapq.heappush(stones, first - second)
       
        return abs(stones[0])