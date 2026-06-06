import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for xy in points:
            x, y = xy[0], xy[1]
            dist = x ** 2 + y ** 2
            heap.append([dist, x, y])
        heapq.heapify(heap)
        res = []
        while k > 0:
            curr = heapq.heappop(heap)
            res.append(curr[1:])
            k -= 1

        return res