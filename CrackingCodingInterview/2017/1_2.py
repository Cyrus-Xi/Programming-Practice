#!/usr/bin/env python

def reverse(a_str):
    if len(a_str) < 2: return a_str
    return a_str[::-1]

def reverse2(a_str):
    if len(a_str) < 2: return a_str

    ret = ''
    for i in xrange(len(a_str)-1,-1,-1):
        ret = ret + a_str[i]

    return ret

# Do it in-place.
def reverse3(a_str):
    if len(a_str) < 2: return a_str

    # Strings are immutable in python.
    a_lst = list(a_str)
    l, r = 0, len(a_str)-1

    while l < r:
        a_lst[l], a_lst[r] = a_lst[r], a_lst[l]
        l += 1
        r -= 1

    return ''.join(a_lst)

assert reverse('abcd') == 'dcba'
assert reverse('bdiez') == 'zeidb'
assert reverse('b') == 'b'
assert reverse('') == ''

assert reverse2('abcd') == 'dcba'
assert reverse2('bdiez') == 'zeidb'
assert reverse2('b') == 'b'
assert reverse2('') == ''

assert reverse3('abcd') == 'dcba'
assert reverse3('bdiez') == 'zeidb'
assert reverse3('b') == 'b'
assert reverse3('') == ''
