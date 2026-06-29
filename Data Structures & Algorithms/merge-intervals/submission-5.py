class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort intervals
        add to stack if none
        compare if ending of last > starting of next merge max ending
        return stack
        """
        intervals.sort(key=lambda interval: interval[0])
        stack = []
        for interval_list in intervals:
            if stack:
                top = stack[-1]
                if top[1] >= interval_list[0]:
                    stack[-1] = [top[0],max(top[1],interval_list[1])]
                else:
                    stack.append(interval_list)
            else:
                stack.append(interval_list)
        return stack

        