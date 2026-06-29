class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        monotonic stack
        keep indexs in stack when u see a higher keep popping and store diffs
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                val = stack.pop()
                result[val] = i - val 
            stack.append(i)
        return result

        