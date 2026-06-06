class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        fruit = time = 0        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fruit += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    queue.append([nr,nc])
                    grid[nr][nc] = 2
                    fruit -= 1
            if queue:
                time += 1 

        return time if fruit == 0 else -1