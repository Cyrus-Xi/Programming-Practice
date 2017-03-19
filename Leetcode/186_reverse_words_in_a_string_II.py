#!/usr/bin/env python

"""
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?
"""

def reverse(arr, l, r):
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1; r -= 1
    
def reverseWords(s):
    """
    @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    @return nothing
    """
    n = len(s)
    l, r = 0, n - 1
    reverse(s, l, r)
    # n + 1 because have to reverse the last word.
    for i in xrange(1, n + 1):
        if i == n or s[i] == ' ':
            reverse(s, l, i - 1)
            l = i + 1
