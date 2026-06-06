class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # we need to start in the top left and go to bottom right via the zeros
        # we can implement a bfs and visit our nodes by changing them to 1's 
            # so we dont go back on it
        # once we reach the end we can return the length at the end if we didnt
        # we will return -1
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append((0,0))
        grid[0][0] = 1
        ROWS, COLS = len(grid), len(grid[0])
        length = 1

        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if r == ROWS-1 and c == COLS -1:
                    return length
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or col < 0 or row == ROWS or col == COLS or
                        grid[row][col] == 1):
                        continue
                    q.append((row,col))
                    grid[row][col] = 1
            length += 1
        return -1


