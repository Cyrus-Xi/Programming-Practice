#!/usr/bin/env python

def countBattleships(self, board):
    """
    :type board: List[List[str]]
    :rtype: int
    """
    num_ships = 0
    
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell != 'X': continue
            # Count the top-left cell of each ship.
            if (not r or board[r-1][c] == '.') and (not c or board[r][c-1] == '.'):
                num_ships += 1
                
    return num_ships
