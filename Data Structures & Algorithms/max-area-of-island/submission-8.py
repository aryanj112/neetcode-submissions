class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        curr = 0
        res = 0
        
        def dfs(r,c):
        
            nonlocal curr
        
            if (r,c) in visit or r == ROWS or c == COLS or r < 0 or c < 0 or grid[r][c] != 1:
                return 
            
            visit.add((r,c))
            curr += 1
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                curr = 0
                if grid[r][c] == 1:
                    dfs(r,c)
                res = max(res,curr)
        return res
