class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort by first value
        l,r pointers going through list if l[1] > r[0] merge l to be l[0],r[1] and then move r up etc
        return len of intervals then
        """
        intervals.sort(key=lambda x: x[0])
        l,r = 0,1
        result = []
        while l < len(intervals):
            currentMax = intervals[l][1]
            while r < len(intervals) and currentMax >= intervals[r][0]:
                currentMax = max(currentMax,intervals[r][1])
                r += 1
            result.append((intervals[l][0],currentMax))
            l = r
            r += 1
        return result