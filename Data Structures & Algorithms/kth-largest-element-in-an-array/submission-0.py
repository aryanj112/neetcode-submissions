import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heap.append(-n)        
        
        heapq.heapify(heap)

        res = None
        while k > 0:
            res = heapq.heappop(heap)
            k -= 1

        return -res
    
