#!/usr/bin/env

def is_uniq_str(a_str):
    # Edge cases.
    if len(a_str) < 2: return True 
    
    # First sort; all dupes will be next to each other.
    a_str = ''.join(sorted(a_str))
    prev = ''

    for i, c in enumerate(a_str):
        if c == prev: return False
        prev = a_str[i]

    return True

def is_uniq_str2(a_str):
    if len(a_str) < 2: return True

    # Use a hashtable / dict.
    exists_dict = {}

    for c in a_str:
        if c in exists_dict: return False
        else: exists_dict[c] = 1

    return True

assert is_uniq_str('abcd')
# a == ''; b == a; c == b; d == c
assert not is_uniq_str('accd')
assert is_uniq_str('d')
assert not is_uniq_str('dacd')

assert is_uniq_str2('abcd')
# a == ''; b == a; c == b; d == c
assert not is_uniq_str2('accd')
assert is_uniq_str2('d')
assert not is_uniq_str2('dacd')

