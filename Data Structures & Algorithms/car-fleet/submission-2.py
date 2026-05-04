import math
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """

        """
        paired = list(zip(position, speed))
        paired.sort(reverse=True)
        stack = []
        print(paired)
        for p, s in paired:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
