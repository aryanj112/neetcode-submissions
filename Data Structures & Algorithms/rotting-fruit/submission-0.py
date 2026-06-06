class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # We want to find all the places where there are rotten fruits
        # BFS on the rotten fruits turning every fresh fruit into rotten
        # if no rotten fruit contains a neighbor then we can simply return
        # if minutes == 0 then -1 else minutes

        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()
        minutes = 0
        fresh = 0

        def appendQ(r,c):
            nonlocal fresh
            if (0 <= r < ROWS and 
                0 <= c < COLS and
                grid[r][c] == 1
            ):
                q.append((r,c))
                grid[r][c] = 2
                fresh -= 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            print("Q", q)
            print("GRID", grid)
            for _ in range(len(q)):
                r, c = q.popleft()
                appendQ(r+1,c)
                appendQ(r-1,c)
                appendQ(r,c+1)
                appendQ(r,c-1)
            minutes += 1

        return minutes if fresh == 0 else -1