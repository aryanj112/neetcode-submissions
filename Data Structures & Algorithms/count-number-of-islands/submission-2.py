class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            while q:
                pr, pc = q.popleft()
                visited.add((pr,pc))
                directions = [[-1,0],[1,0],[0,-1],[0,1]]
                for dr, dc in directions:
                    nr, nc = dr + pr, dc + pc
                    if (0 <= nr < ROWS and
                        0 <= nc < COLS and 
                        grid[nr][nc] == "1" and (nr,nc) not in visited):
                        q.append((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    res += 1
        return res

# visited = []

# 0,1

# [["0","1","1","1","0"],
#  ["0","1","0","1","0"],
#  ["1","1","0","0","0"],
#  ["0","0","0","0","0"]]

