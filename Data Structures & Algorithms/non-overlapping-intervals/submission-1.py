class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        last_interval_end_point = intervals[0][1]

        for i in range(1, len(intervals), 1):
            # This means it is overlapping because if the last interval ends further
            # than where the next one starts thats an overlap
            if last_interval_end_point > intervals[i][0]:
                res += 1
                # pick the smallest end point so we have the inteval that corrupts
                # the least amount of intervals
                last_interval_end_point = min(intervals[i][1], last_interval_end_point)
            else:
                # else we want to update where the last value ends and then this will
                # allow us to check the next ones
                last_interval_end_point = intervals[i][1]

        return res
              