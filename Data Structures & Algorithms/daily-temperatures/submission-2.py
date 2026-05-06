class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        make a monotonic stack
        create results array with 0 for all 
        go through temp list either
        1) add value to last seen highest
        2) while current val is higher than top of stack pop update results
        """
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i in range(n):
            c = temperatures[i]
            while stack and c > stack[-1][0]:
                lc,li = stack.pop()
                result[li] = i - li
            stack.append((c,i))
        return result
                    


        
        
        