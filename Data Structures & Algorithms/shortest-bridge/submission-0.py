class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS or 
               (r,c) in visit or grid[r][c] == 0):
                return
            
            visit.add((r,c))            
            dfs(r,c+1)
            dfs(r,c-1)
            dfs(r+1,c)
            dfs(r-1,c)
        
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if not found and grid[r][c] == 1:
                    dfs(r,c)
                    found = True
        
        q = deque()
        for val in visit:
            q.append(val)
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        bridge = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr,dc in directions:
                    nr, nc = dr + r, dc + c
                    if (nr < 0 or nc < 0 or nr == ROWS or nc == COLS or 
                    (nr,nc) in visit):
                        continue
                    if grid[nr][nc] == 1:
                        return bridge
                    q.append((nr,nc))
                    visit.add((nr,nc))
            bridge += 1
        return bridge