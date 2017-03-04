#!/usr/bin/env python

def max_duffel_bag_value(cake_tuples, cap):
    max_value_at = [0] * cap + 1

    for c in xrange(cap + 1):
        for cake_weight, cake_value in cake_tuples:
            # Return infinity if cake exists with 0 weight and positive value.
            if not cake_weight and cake_value: return float('inf')
            curr_max = max_value_at[c]
            if cake_weight == c:
                max_value_at[c] = max(curr_max, cake_value)
            elif cake_weight < c:
                cand_max = cake_value + max_value_at[c - cake_weight]
                max_value_at[c] = max(curr_max, cand_max) 

    return max_value_at[cap]
