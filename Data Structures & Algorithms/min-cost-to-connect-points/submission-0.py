class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:    
        edges = {(x,y):[] for x, y in points}
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                cost = abs(x1 - x2) + abs(y1 - y2)
                edges[(x1,y1)].append([cost,x2,y2])
                edges[(x2,y2)].append([cost,x1,y1])

        res = 0
        visit = set()
        minHeap = [(0,points[0][0],points[0][1])]
        while len(visit) < len(points):
            dist1, x1, y1 = heapq.heappop(minHeap)
            if (x1,y1) in visit:
                continue
            res += dist1
            visit.add((x1,y1))
            for dist2, x2, y2 in edges[x1, y1]:
                if (x2,y2) not in visit:
                    heapq.heappush(minHeap, (dist2,x2,y2))
        return res