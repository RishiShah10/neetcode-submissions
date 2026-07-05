class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        go through temperatures
        if stack is empty store
        else compare to end of stakc if current is higher pop the index calculate diff write to result
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            if not stack:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temperatures[i]:
                val = stack.pop()
                result[val] = i - val
            stack.append(i)
        return result
