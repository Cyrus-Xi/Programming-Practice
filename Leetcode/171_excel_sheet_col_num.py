#!/usr/bin/env python

def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    # Do base 26 number math.
    return sum([26 ** (len(s)-i-1) * (ord(c)-64) for i, c in enumerate(s)])
