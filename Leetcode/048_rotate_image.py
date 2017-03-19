#!/usr/bin/env python

"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""

def rotate(self, A):
    # Reverse and transpose.
    A[:] = zip(*A[::-1])
