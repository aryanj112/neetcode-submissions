class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()
        def dfs(r, c):
            area = 0
            q = collections.deque()
            q.append((r,c))
            while q:
                pr, pc = q.popleft()
                directions = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]
                for dr,dc in directions:
                    nr, nc = dr + pr, dc + pc
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and
                        grid[nr][nc] == 1 and
                        (nr,nc) not in visited):
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    res = max(res, dfs(r, c))
        return res