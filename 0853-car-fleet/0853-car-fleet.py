class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pairs)[::-1]:
            time = (target-p) / s
            if not stack or (stack and time > stack[-1]):
                stack.append(time)
            # else do nothing
        return len(stack)