#!/usr/bin/env python

"""
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def lengthOfLongestSubstring(self, s):
    max_l, arr = 0, []
    for c in s:
        if c in arr:
            # Strip out the arr containing the dupe of c.
            try: arr = arr[arr.index(c) + 1:]
            except IndexError: arr = []
        arr.append(c)
        max_l = max(max_l, len(arr))
    return max_l
