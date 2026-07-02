class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort them off start if none in stack add
        if stack then check stack and if can merge pop add merged if cnt add newest return stack
        """
        stack = []
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)
        for i in intervals:
            if stack and stack[-1][1] >= i[0]:
                stack[-1][1] = max(stack[-1][1],i[1])
            else:
                stack.append(i)
        return stack
        