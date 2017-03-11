#!/usr/bin/env python

def is_in_list(arr, num):
    if arr[0] > num or num > arr[-1]: return False
    low, high = 0, len(arr) - 1
    while low < high:
        mid = low + ((high - low) / 2)
        if num == arr[mid]: return True
        elif num > arr[mid]: low = mid + 1
        elif num < arr[mid]: high = mid
    
    return False
