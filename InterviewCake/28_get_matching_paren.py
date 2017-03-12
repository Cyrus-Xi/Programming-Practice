#!/usr/bin/env python

def get_matching_paren(s, pos):
    # Proxy stack variable.
    num_l = 0
    for i, ch in enumerate(s):
        # Can skip ahead past the position of the left paren I'm given.
        if i <= pos: continue
        if ch == '(': 
            num_l += 1
        elif ch == ')':
            if not num_l: return i
            else: num_l -= 1
    return None

s = ("Sometimes (when I nest them (my parentheticals) too much "
     + "(like this (and this))) they get confusing.")
assert s[10] == '(' and s[28] == '('
assert get_matching_paren(s, 10) == 79
assert get_matching_paren(s, 28) == 46
assert s[79] == ')' and s[46] == ')'
assert not get_matching_paren('( just 1 lonely paren', 0)
print 'Tests passed!'
