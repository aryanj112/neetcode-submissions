class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                directions = [[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and
                        (nr,nc) not in visited and
                        grid[nr][nc] != -1):
                        visited.add((nr,nc))
                        q.append((nr,nc))
            dist += 1
        