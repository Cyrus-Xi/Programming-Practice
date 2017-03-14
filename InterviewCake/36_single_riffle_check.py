#!/usr/bin/env python

def is_single_riffle(shuffled_d, h1, h2):
    if len(shuffled_d) < 2: return True
    # To adhere to DRY.
    h_arr = [h1, h2]
    h_idxes = [0, 0]
        
    for s in shuffled_d:
        if s not in h1 and s not in h2: return False
        h_idx = 0 if s in h1 else 1
        idx = h_arr[h_idx].index(s)
        # Shuffled deck can't have cards from a given half out of order.
        if idx < h_idxes[h_idx]: return False
        h_idxes[h_idx] += 1
    
    # Both halves have to be "exhausted."
    return h_idxes[0] == len(h1) and h_idxes[1] == len(h2)
    
assert is_single_riffle([2, 3, 1, 4, 5], [3, 4, 5], [2, 1])
assert not is_single_riffle([2, 3, 1, 4, 5], [3, 4, 2], [2, 5])
assert not is_single_riffle([1, 2, 3], [2], [3, 1])
print 'Tests passed!'
