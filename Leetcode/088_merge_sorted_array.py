#!/usr/bin/env python

def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    i2 = 0
    if not nums2: return
    
    for i, num in enumerate(nums1):
        # Add on leftover elements.
        if i >= m:
            nums1[i] = nums2[i2]
            i2 += 1
            continue
        if num <= nums2[i2]: 
            continue
        else:
            # Swap.
            tmp = num
            nums1[i] = nums2[i2]
            nums2[i2] = tmp
            nums2.sort()
