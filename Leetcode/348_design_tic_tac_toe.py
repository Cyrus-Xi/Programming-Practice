class TicTacToe(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [[0] * n, [0] * n]
        self.cols = [[0] * n, [0] * n]
        self.d1 = [0, 0]
        self.d2 = [0, 0]

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        p = player - 1
        self.rows[p][row] += 1
        self.cols[p][col] += 1
        # Increment diagonals, both if middle cell (e.g., if n = 5, (2, 2)).
        if row == col: self.d1[p] += 1
        if row + col == self.n - 1: self.d2[p] += 1
            
        return (player if any(x[i] == self.n for x, i in zip((self.rows[p], self.cols[p]), (row, col)))
                            or self.d1[p] == self.n or self.d2[p] == self.n
                            else 0)
