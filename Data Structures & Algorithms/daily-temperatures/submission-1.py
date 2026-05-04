class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                value = stack.pop()
                result[value[0]] = i - value[0]
            stack.append((i,temp))
        return result
            
        