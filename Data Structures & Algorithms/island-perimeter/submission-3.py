class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        def dfs(r,c):
            print(r,c)
            print(visit)
            if (r,c) in visit:
                return 0
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1
            curr = 0
            visit.add((r,c))
            curr += dfs(r-1,c) # up (first case + 1)
            curr += dfs(r,c-1) # left (first case + 1)
            curr += dfs(r+1,c) # down (first case is whatever is from the bottom)
            curr += dfs(r,c+1)
            return curr
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return dfs(r,c)

[0,1,0,0]
[1,1,1,0]
[0,1,0,0]
[1,1,0,0]
