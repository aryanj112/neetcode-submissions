class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]
        curr = 0

        for start, end in intervals[1:]:
            curr_start, curr_end = res[curr]
            print(start,end)
            if start <= curr_end and start >= curr_start:
                res[curr][1] = max(curr_end, end)
            else:
                res.append([start,end])
                curr += 1
        return res