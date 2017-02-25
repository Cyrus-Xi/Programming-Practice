#!/usr/bin/env python

def find_rotation_pt(arr):
    if not arr: return None
    low, high = 0, len(arr) - 1
    # Check if fully sorted / not rotated.
    if arr[low] <= arr[high]: return 0
    
    while low < high:
        mid = low + (high - low) / 2
        if arr[low] <= arr[mid]: low = mid + 1
        else: high = mid
    
    return low
        
words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

nums = [4, 5, 6, 7, 8, 1, 2, 3]
nums2 = [1, 2, 3, 4, 5, 6, 7, 8]
assert find_rotation_pt(words) == 4
assert find_rotation_pt(nums) == 5
assert find_rotation_pt(nums2) == 0
print "Tests pass!"

