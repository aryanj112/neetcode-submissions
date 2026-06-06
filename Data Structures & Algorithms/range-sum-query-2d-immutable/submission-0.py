class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.areaSum = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        print(self.areaSum)
        
        for i in range(1, ROWS + 1, 1):
            for j in range(1, COLS + 1, 1):
                self.areaSum[i][j] = (matrix[i - 1][j - 1] + self.areaSum[i][j - 1] +
                self.areaSum[i - 1][j] - self.areaSum[i - 1][j - 1])

        print(self.areaSum)
        #                     i, j -1    i - 1,j   i -1, j -1   
        # bottom_right + bottom_left + top_right - top_left 
        #     Matrix       areaSum.........
        '''
            [3, 0, 1, 4, 2]
            [5, 6, 3, 2, 1] 
            [1, 2, 0, 1, 5] 
            [4, 1, 0, 1, 7] 
            [1, 0, 3, 0, 5]

            [0, 0, 0, 0, 0, 0]
            [0, 3, 0, 1, 4, 2]
            [0, 5, 6, 3, 2, 1] 
            [0, 1, 2, 0, 1, 5] 
            [0, 4, 1, 0, 1, 7] 
            [0, 1, 0, 3, 0, 5]
        
        '''






    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (self.areaSum[row2][col2] - self.areaSum[row1 - 1][col2]
         - self.areaSum[row2][col1 - 1] + self.areaSum[row1 - 1][col1 - 1])








    
    
    
    
    
    
    '''
          0  1  2  3  4  5  6
    0    [0, 0, 0, 0, 0, 0, 0]    
    1    [0, 9, 1, 1, 2, 8, 5]
    2    [0, 5, 6, 7, 8, 9, 1]
    3    [0, 1, 2, 3, 4, 4, 9]
    4    [0, 1, 2, 3, 4, 6, 3]
    5    [0, 3, 1, 8, 4, 5, 2]


          0  1  2  3  4  5
    0    [9, 1, 1, 2, 8, 5]
    1    [5, 6, 7, 8, 9, 1]
    2    [1, 2, 3, 4, 4, 9]
    3    [1, 2, 3, 4, 6, 3]
    4    [3, 1, 8, 4, 5, 2]

    where row1 = 0, col1 = 0 | row2 = 0, col2 = 0
    
    Area(row2, col2)
    - Area(row1 - 1, col2)
    - Area(row2, col1 - 1)
    Area(row1 - 1, col1 - 1)

    '''