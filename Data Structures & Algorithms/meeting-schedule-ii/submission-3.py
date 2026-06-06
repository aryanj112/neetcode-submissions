"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        minHeap = []
        heapq.heappush(minHeap, intervals[0].end)
        # minHeap has the fist end time of the meetings
        for i in range(1,len(intervals), 1):
            curr_end = minHeap[0]
            if curr_end > intervals[i].start:
                heapq.heappush(minHeap, intervals[i].end)
            else:
                # curr_end <= intervals[i][0] therefor no conflict we can schedule on that day
                curr_end = intervals[i].end
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, curr_end)
        return len(minHeap)

        # first sort the array
        # go through the array and if we see a conflict create a new day
        # store the current end date of the day as the key in a min heap
