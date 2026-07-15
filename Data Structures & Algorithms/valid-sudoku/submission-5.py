class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for row in range(9):
            hashset = set()
            for col in range(9):
                if board[row][col] in hashset and board[row][col] != ".":
                    return False
                hashset.add(board[row][col])
        print("ROWS ARE FINE")        

        # check cols
        for col in range(9):
            hashset = set()
            for row in range(9):
                if board[row][col] in hashset and board[row][col] != ".":
                    return False
                hashset.add(board[row][col])
        print("COLS ARE FINE")        

        def check_box(row,col):
            # given a row and col coordinate check a box around it
            print("here", row,col)
            hashset = set()
            for i in range(3):
                for j in range(3):
                    if board[row+i][col+j] in hashset and board[row+i][col+j] != ".":
                        return False
                    hashset.add(board[row+i][col+j])
            print(hashset)
            print(row,col,"IS FINE")     
            return True   

        # check boxes
        for row in [0,3,6]:
            for col in [0,3,6]:
                print("checking", row, col)
                if not check_box(row,col):
                    return False
        print("BOARD IS FINE")        

        return True
        