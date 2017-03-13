#!/usr/bin/env python

def get_dupe_num_to_n(nums, n):
    # Use sum of nums to n formula to get O(1) space.
    return sum(nums) - n * (n + 1) / 2
    
assert get_dupe_num_to_n([1, 2, 3, 3, 4, 5], 5) == 3
print 'Test passed!'
