"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        1) lets sort the intervals list by the starting value
        two pointer l = 0 r = 1 moving 1+ until r == len(intervals) - 1
        if l[1] > r[0] return false
        """
        intervals.sort(key=lambda x: (x.start, x.end))
        l,r = 0,1
        while r <= len(intervals) - 1:
            if intervals[l].end > intervals[r].start:
                return False
            l += 1
            r += 1
        return True