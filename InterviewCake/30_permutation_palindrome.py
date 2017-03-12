#!/usr/bin/env python

def is_permutation_palindrome(s):
    if len(s) < 2: return True
    odds = set()
    for ch in s:
        if ch in odds: odds.remove(ch)
        else: odds.add(ch)
    # For a permutation to be a palindrome, can only have 0-1 chars
    # with an odd frequency.
    return len(odds) < 2
            
s1, s2, s3, s4, s5 = 'civic', 'ivicc', 'civil', 'livci', 'aaa'
assert is_permutation_palindrome(s1)
assert is_permutation_palindrome(s2)
assert not is_permutation_palindrome(s3)
assert not is_permutation_palindrome(s4)
assert is_permutation_palindrome(s5)
print 'Tests passed!'
