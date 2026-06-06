class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # given that we have a sorted array we want to go from the first interval
        # add it to the res and then keep iterating until we get out of the zone
        # then add it to res and then iterate from there
        intervals.sort()
        curr = 0
        res = [intervals[0]]
        for i in range(len(intervals)):
            s, e = intervals[i][0], intervals[i][1]
            rs, re = res[curr][0], res[curr][1]

            if (s >= rs and s <= re) or (rs >= s and rs <= e):
                res[curr][0] = min(s, rs)
                res[curr][1] = max(e, re)
            else:
                res.append([s,e])
                curr += 1
        return res

