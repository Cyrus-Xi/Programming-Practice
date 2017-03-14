#!/usr/bin/env python

import random

def inplace_shuffle(lst):
    n = len(lst)
    if n < 2: return lst
    for i in xrange(n - 1):
        repl = random.randint(i, n - 1)
        if i != repl: lst[i], lst[repl] = lst[repl], lst[i]
        
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inplace_shuffle(lst)
print lst
