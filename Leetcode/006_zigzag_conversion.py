#!/usr/bin/env python

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

def convert(self, s, numRows):
    # The key is that the distance down then up (or up then down) to get to the next letter on the current row is symmetric regardless of the horizontal distance traveled / the diagonal.
    linenum = 1
    # N-1 + N-1 (4), Xth line starts w Xth char, N-X + N-X / X-1 + X-1 (down-up or up-down; the distance is the same), 3rd line starts w 3rd char and is X-1 + X-1
    ret_str = ''
    ind = 0
    # Have to alternate strategy for middle lines.
    mid_cycle_index = 1
    if numRows == 1: return s
    for i in xrange(len(s)):
        ret_str += s[ind]
        # First line.
        if linenum == 1:
            ind += 2 * (numRows - 1)
        elif linenum == numRows:
            ind += 2 * (linenum - 1)
        else:
            if mid_cycle_index % 2 == 1:
                ind += 2 * (numRows - linenum)
            else:
                ind += 2 * (linenum - 1)
            mid_cycle_index += 1
        # Go to next line.
        if ind >= len(s):
            linenum += 1
            ind = linenum - 1  # ind is 0-based, linenum 1-based
            mid_cycle_index = 1
    return ret_str
