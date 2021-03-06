#!/usr/bin/env python

def maxSubArray(self, nums):
    if not nums: return nums

    max_so_far = max_end_here = nums[0]
    for n in nums[1:]:
        # No max subarray will include a negative sum prefix, because 
        # could have greater sum if just leave prefix off.
        # So if the current number is greater than the previous sum plus the
        # current number, don't include the previous sum / start over.
        max_end_here = max(n, max_end_here + n)
        max_so_far = max(max_so_far, max_end_here)
            
    return max_so_far
