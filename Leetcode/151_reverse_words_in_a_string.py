#!/usr/bin/env python

"""
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".
"""

def reverseWords(self, s):
    return " ".join(s.split()[::-1])
