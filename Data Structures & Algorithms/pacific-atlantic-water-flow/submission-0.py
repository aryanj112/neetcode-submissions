class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def bfs(r,c,visited):
            q = collections.deque()
            q.append((r,c))
            while q:
                pr,pc = q.popleft()
                directions = [[0,0],[0,1],[0,-1],[1,0],[-1,0]]
                for dr, dc in directions:
                    nr, nc = pr + dr, pc + dc
                    if (0 <= nr < ROWS and 
                        0 <= nc < COLS and
                        heights[pr][pc] <= heights[nr][nc] and
                        (nr,nc) not in visited
                    ): 
                        visited.add((nr,nc))
                        q.append((nr,nc))

        for c in range(COLS):
            bfs(0,c, pac)
            bfs(ROWS - 1,c, atl)
        for r in range(ROWS):
            bfs(r,0, pac)
            bfs(r,COLS-1, atl)

        res = []
        for cell in pac:
            if cell in atl:
                res.append(cell)

        return res
        