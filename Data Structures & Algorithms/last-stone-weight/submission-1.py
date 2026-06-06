import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        
        for n in stones:
            heapq.heappush(heap, -n)

        while len(heap) > 1:
            print(heap)
            r1 = -(heapq.heappop(heap))
            r2 = -(heapq.heappop(heap))

            val = abs(r1 - r2)
            if val:
                heapq.heappush(heap, -val)
            heapq.heapify(heap)
            print(heap)


        return 0 if len(heap) == 0 else -heap[0]
        