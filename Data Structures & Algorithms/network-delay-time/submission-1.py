class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for u, v, t in times:
            edges[u].append((v,t))

        minHeap = [(0,k)]
        visit = set()
        res = 0

        while minHeap:
            t1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            res = max(res,t1)
            for neighbor, weight in edges[n1]:
                if neighbor not in visit:
                    heapq.heappush(minHeap,(weight + res, neighbor))
        if len(visit) != n:
            return -1
        return res
        

