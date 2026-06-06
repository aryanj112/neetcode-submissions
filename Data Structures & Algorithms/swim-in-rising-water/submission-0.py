class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        minHeap = [(grid[0][0],0,0)]
        time = grid[0][0]
        while minHeap:
            print(minHeap)
            h, r, c = heapq.heappop(minHeap)
            time = max(time,h)
            if r == ROWS - 1 and c == COLS - 1:
                return time
            visit.add((r,c))
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (0 <= nr < ROWS) and (0 <= nc < COLS) and (nr,nc) not in visit:
                    heapq.heappush(minHeap, (grid[nr][nc],nr,nc))
        return time