#!/usr/bin/env python

def highest_product_three(lst_ints):
    # Naive is sort but doesn't handle negatives well and is at least O(N log N).
    # We have a O(N) greedy solution. Just need to store some state.
    highest_prod_3 = highest_prod_2 = lowest_prod_2 = 1
    highest = lowest = lst_ints[0]
    
    for i, num in enumerate(lst_ints[1:]):
        # Need 3 nums.
        # lowest_prod_2 in the case of negatives.
        if i > 0:
            highest_prod_3 = max(highest_prod_3, num * highest_prod_2, num * lowest_prod_2)
        # Update the prod_2's.
        highest_prod_2 = max(highest_prod_2, num * highest, num * lowest)
        lowest_prod_2 = min(lowest_prod_2, num * lowest, num * highest)
        # Then highest/lowest.
        highest = max(highest, num)
        lowest = min(lowest, num)

    return highest_prod_3

print highest_product_three([2, 3, 6, 5])
print highest_product_three([-10, -10, 1, 3, 2])
print highest_product_three([1, 10, -5, 1, -100])
