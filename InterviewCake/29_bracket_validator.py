#!/usr/bin/env python

def is_valid_brackets(s):
    mp = {')': '(', '}': '{', ']': '['}
    # Separate vals set for O(1) membership checking.
    vals = set(mp.values())
    stk = []
    
    for ch in s:
        if ch in vals:
            stk.append(ch)
        elif ch in mp:
            # Don't pop unless we know it's a match.
            if not stk or stk[-1] != mp[ch]: return False
            stk.pop()
    
    return not stk

assert is_valid_brackets('{[]()}')
assert not is_valid_brackets('{[(])}')
assert not is_valid_brackets('{[}')
print 'Tests passed!'
