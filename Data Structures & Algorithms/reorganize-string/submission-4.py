class Solution:
    def reorganizeString(self, s: str) -> str:
        # first get an amount of characters
            # a: 1 x: 1 y : 2

        # put these in a heap
        # then we can pop the max element and store in a queue that will get put back in
        # after one round
        
        # y 

        # how to ensure that we dont get a repeat

        # prev 
        hashMap = defaultdict(int)
        for c in s:
            hashMap[c] += 1
        
        maxHeap = []
        for c, amt in hashMap.items():
            heapq.heappush(maxHeap, [-amt, c])

        # inverse counts by -1
        res = ""
        prev = ""

        while maxHeap:
            amt, c = heapq.heappop(maxHeap)
            if c == prev:
                if not maxHeap:
                    return ""
                amt_second, c_second = heapq.heappop(maxHeap)
                res += c_second
                print(res)
                print(maxHeap)

                if amt_second + 1 != 0:
                    heapq.heappush(maxHeap, [amt_second + 1, c_second])
                prev = c_second
            else:
                res += c
                amt += 1 
                prev = c
            if amt != 0:
                heapq.heappush(maxHeap, [amt,c])
        return res