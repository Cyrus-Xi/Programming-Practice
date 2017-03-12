#!/usr/bin/env python

def reverse_str(s):
    # Convert to list since Python strings are immutable.
    lst_s = list(s)
    l, r = 0, len(lst_s) - 1
    while l < r:
        lst_s[l], lst_s[r] = lst_s[r], lst_s[l]
        l, r = l + 1, r - 1
    return ''.join(lst_s)

assert reverse_str('reversed') == 'desrever'
print 'Test passed!'
