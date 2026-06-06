class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        res = 0
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        def dfs(r,c):
            if (r,c) in visit or r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 
            
            visit.add((r,c))
            q.append([r,c])

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break
            if found:
                break
        
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr,nc) in visit or nr < 0 or nc < 0 or nr == ROWS or nc == COLS:
                        continue

                    if grid[nr][nc] == 1 and (nr,nc) not in visit:
                        return res
                    q.append([nr,nc])
            res += 1


        print(visit)

        return res
