#!/usr/bin/env python

def gen_permutations(s):
    if len(s) < 2: return set([s])
    new_perms = gen_permutations(s[1:])
    perms = set()
    for p in new_perms:
        # Add the first character at each position in the permutation.
        for i in xrange(len(p) + 1):
            new_p = p[:i] + s[0] + p[i:]
            perms.add(new_p)
    return perms
                         
print gen_permutations('abc')
