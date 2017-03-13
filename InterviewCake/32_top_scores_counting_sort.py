#!/usr/bin/env python

import itertools

def sort_scores(scores, max_score):
    # Use counting sort to get O(n) time at the expense of O(n) space.
    arr = [0] * (max_score + 1)
    for sc in scores:
        arr[sc] += 1
    # Need to handle multiple players with the same score.
    srted = [[i] * n for i, n in enumerate(arr) if n]
    # Flatten.
    return list(itertools.chain(*srted))

unsorted_scores = [37, 89, 91, 41, 65, 91, 53]
MAX_SCORE = 100
assert sort_scores(unsorted_scores, MAX_SCORE) == [37, 41, 53, 65, 89, 91, 91]
print 'Test passed!'
