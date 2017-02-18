#!/usr/bin/env python

def get_products_of_all_except_at(list_ints):
    """
    Naive solution is to, for each number, iterate through the rest of the 
    list and multiply. O(N^2)
    If allowed division, could get product of all ints then just divide by each num.
    Intuition: the product at index i is just the product of the nums before it 
    times the product of the nums after it.
    """
    if len(list_ints) < 2: 
        raise Exception('list_ints needs at least 2 elements')
    
    prev_prod = 1
    prods_before = []
    for num in list_ints:
        prods_before.append(prev_prod)
        prev_prod *= num
        
    prod_after = 1
    i = len(prods_before) - 1    
    while i >= 0:
        prods_before[i] = prods_before[i] * prod_after
        prod_after *= list_ints[i]
        i -= 1
        
    return prods_before

print get_products_of_all_except_at([1, 7, 3, 4])
print get_products_of_all_except_at([1, 2, 6, 5, 9])
print get_products_of_all_except_at([2])

