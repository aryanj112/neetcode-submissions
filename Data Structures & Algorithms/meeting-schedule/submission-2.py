"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
    
    # conflict would be defined as some sort of overlap such that the 
    # start time of an interval is less than the end time of another interval (ascending)

    # (0,30) and (5, 10) are conflicting because s1 < s2 < e1 or s2 < s1 < e2
    # (5, 10) and (0, 30)

    # we want to iterate through the entire array and then keep checking pairs
    # if these conditions: s1 < s2 < e1 or s2 < s1 < e2 ever mark true then we know
    # we have some sort of an overlap -> return false
    # at the very end we can simply return true because we know it is ok

        l, r = 0, 1

        while r < len(intervals):
            s1, e1 = intervals[l].start, intervals[l].end
            s2, e2 = intervals[r].start, intervals[r].end
            if (s2 >= s1 and s2 < e1) or (s1 >= s2 and s1 < e2):
                return False
            l += 1
            r += 1
        return True


