#!/usr/bin/env python

"""
Don't Get Volunteered!
======================

As a henchman on Commander Lambda's space station, you're expected to be resourceful, smart, and a quick thinker. It's not easy building a doomsday device and capturing bunnies at the same time, after all! In order to make sure that everyone working for her is sufficiently quick-witted, Commander Lambda has installed new flooring outside the henchman dormitories. It looks like a chessboard, and every morning and evening you have to solve a new movement puzzle in order to cross the floor. That would be fine if you got to be the rook or the queen, but instead, you have to be the knight. Worse, if you take too much time solving the puzzle, you get "volunteered" as a test subject for the LAMBCHOP doomsday device!

To help yourself get to and from your bunk every day, write a function called answer(src, dest) which takes in two parameters: the source square, on which you start, and the destination square, which is where you need to land to solve the puzzle.  The function should return an integer representing the smallest number of moves it will take for you to travel from the source square to the destination square using a chess knight's moves (that is, two squares in any direction immediately followed by one square perpendicular to that direction, or vice versa, in an "L" shape).  Both the source and destination squares will be an integer between 0 and 63, inclusive, and are numbered like the example chessboard below.
"""

from collections import deque

def answer(src, dest):
    if src == dest: return 0

    # Build chessboard.
    matrix = []
    up_to = 8
    for i in xrange(8):
        row = [i for i in xrange(up_to - 8, up_to)]
        matrix.append(row)
        up_to += 8
        
    potentials = [(-2, 1), (-2, -1), (2, 1), (2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2)]

    # Get row, col of src.
    for r, row in enumerate(matrix):
        for c, col in enumerate(row):
            if col == src: start = (r, c, 0)

    # Want shortest path, so do BFS with a queue.
    jumps = deque([start])
    r, c, lvl = jumps[0]
    visited = []

    while jumps:
        r, c, lvl = jumps.popleft()
        if matrix[r][c] == dest: return lvl
        visited.append((r, c))
        # Each time we add a neighbor, the # of moves is current lvl + 1.
        # Need to make sure we only add moves that stay in-bounds and don't repeat.
        moves = [(r, c, lvl+1) for r, c in [(r+i, c+j) for i, j in potentials] 
                if (r, c) not in visited and r > -1 and r < 8 and c > -1 and c < 8]
        jumps.extend(moves)
    
    return -1

assert answer(19, 36) == 1
assert answer(0, 1) == 3
assert answer(50, 45) == 2

