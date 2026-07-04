class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows,cols = len(matrix), len(matrix[0])
        self.ROWS = rows
        self.COLS = cols

        sums = [[0 for _ in range(cols)] for _ in range(rows)]
        for r in range(rows - 1, -1 ,-1):
            for c in range(cols - 1, -1, -1):
                if c + 1 == cols and r + 1 == rows: # bottom right
                    sums[r][c] = matrix[r][c]
                elif c + 1 == cols:
                    # right side
                    sums[r][c] = matrix[r][c] + sums[r+1][c]
                elif r + 1 == rows:
                    # bottom side
                    sums[r][c] = matrix[r][c] + sums[r][c+1]
                else:                
                    sums[r][c] = matrix[r][c] + sums[r][c+1] + sums[r+1][c] - sums[r+1][c+1]
        self.ans = sums

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if col2 + 1 == self.COLS and row2 + 1 == self.ROWS: # bottom right
            return self.ans[row1][col1]
        elif col2 + 1 == self.COLS:
            # right side
            return self.ans[row1][col1] - self.ans[row2+1][col1]
        elif row2 + 1 == self.ROWS:
            # bottom side
            return self.ans[row1][col1] - self.ans[row1][col2+1]
        else:                
            return self.ans[row1][col1] - self.ans[row2+1][col1] - self.ans[row1][col2+1] + self.ans[row2+1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)