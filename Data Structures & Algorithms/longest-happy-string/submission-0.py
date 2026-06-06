class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = ""
        maxHeap = []
        if a != 0:
            maxHeap.append([-a, "a"])
        if b != 0:
            maxHeap.append([-b, "b"])
        if c != 0:
            maxHeap.append([-c, "c"])
        heapq.heapify(maxHeap)
        invalid = None
        
        while maxHeap or invalid:
            if invalid and not maxHeap:
                return res
           
            freq, char = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                invalid = [freq, char]
            else:
                res += char
                freq += 1
                if invalid:
                    heapq.heappush(maxHeap, invalid)
                    invalid = None
                if freq < 0:
                    heapq.heappush(maxHeap, [freq , char])
        return res