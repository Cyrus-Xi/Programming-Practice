#!/usr/bin/env python

import sys

# Without just doing: return max(arr)
def get_max(arr):
    if len(arr) < 2: return arr

    return sorted(arr)[-1] 

# Without sorting.
def get_max2(arr):
    if len(arr) < 2: return arr

    max_yet = arr[0]
    for e in arr:
        if e > max_yet: max_yet = e

    return max_yet

assert get_max([1, 3, 7, 2]) == 7
assert get_max([2, 2]) == 2
assert get_max([]) == []

assert get_max2([1, 3, 7, 2]) == 7
assert get_max2([2, 2]) == 2
assert get_max2([]) == []


def min_diff(arr):
    if len(arr) < 2: return 0
    
    arr = sorted(list(set(arr)))
    # Can't be 0 because that could be the minimum difference.
    min_diff = sys.maxint
    # Can't be arr[0] because 0 could be min diff, again.
    prev = arr[1]

    for i, e in enumerate(arr):
        diff = abs(e - prev)
        if diff < min_diff: min_diff = diff
        prev = arr[i]

    return min_diff

assert min_diff([4, 10, 7, -2, 3]) == 1
assert min_diff([2, 10]) == 8


# Sort then work inward. O(n log n) time, O(1) space.
# Output will be the pairs.
# Assume can remove dupes.
def get_pairs_sum_to_k(arr, k):
    if len(arr) < 2: return None

    arr = sorted(set(arr))

    out_arr = []
    i, j = 0, len(arr) - 1

    while i < j:
        cand = arr[i] + arr[j]

        if cand == k: 
            out_arr.append((arr[i], arr[j]))
            i += 1
        elif cand > k: j -= 1
        elif cand < k: i += 1

    return sorted(out_arr, key = lambda x: x[0])

# Do it in one pass, O(N) time, using a hash table, O(N) space.
def get_pairs_sum_to_k2(arr, k):
    if len(arr) < 2: return None

    complements = {}
    arr = list(set(arr))
    out_arr = []

    for e in arr:
        if k - e in complements:
            out_arr.append((e, k-e))
        else:
            complements[e] = 1

    return out_arr

assert get_pairs_sum_to_k([0, 3, 2, 1, 4, 9], 5) == [(1, 4), (2, 3)]
assert get_pairs_sum_to_k2([0, 3, 2, 1, 4, 9], 5) == [(3, 2), (4, 1)]





    




        
        





