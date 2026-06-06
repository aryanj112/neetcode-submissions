class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row_servers = defaultdict(set) # maps row index to server indexes
        col_servers = defaultdict(set) # maps row index to server indexes
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    row_servers[r].add(c)
                    col_servers[c].add(r)
        count = 0      
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (len(row_servers[r]) > 1 or len(col_servers[c]) > 1):
                    count += 1
        return count