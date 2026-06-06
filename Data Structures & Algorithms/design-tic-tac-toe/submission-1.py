class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.antidiagonal = 0
        self.n = n
        # player 1 = +1
        # player 2 = -1

    def move(self, row: int, col: int, player: int) -> int:
        delta = 1
        n = self.n

        if player == 2:
            delta = -1

        self.rows[row] += delta
        self.cols[col] += delta

        if row == col:
            self.diagonal += delta
        if row + col == n - 1:
            self.antidiagonal += delta
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.antidiagonal) == n:
            return player
        else:
            return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
