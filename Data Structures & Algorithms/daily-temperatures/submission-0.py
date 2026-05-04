class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        """
        result = [0] * len(temperatures)
        stack = []
        for i in range((len(temperatures))):
            while stack and stack[-1][1] < temperatures[i]:
                value = stack.pop()
                print(value)
                result[value[0]] = i - value[0]
            stack.append((i,temperatures[i]))
            print(stack)
        return result