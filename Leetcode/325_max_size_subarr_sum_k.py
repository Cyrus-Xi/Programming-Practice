#!/usr/bin/env python

def maxSubArrayLen(self, nums, k):
    sum_dict = {0: -1}
    ans = acc = 0
    for i, num in enumerate(nums):
        acc += num
        if acc not in sum_dict: sum_dict[acc] = i
        if acc-k in sum_dict:
            ans = max(ans, i - sum_dict[acc-k])
        
    return ans
