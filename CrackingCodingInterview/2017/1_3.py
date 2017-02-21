#!/usr/bin/env python

# Can sort, if same then permutation.
def is_permutation(str1, str2):
    return ''.join(sorted(str1)) == ''.join(sorted(str2))

# If can't sort, determine using char frequencies.
def is_permutation2(str1, str2):
    dict1, dict2 = {}, {}

    for c in str1:
        dict1[c] = dict1.get(c, 0) + 1

    for c in str2:
        dict2[c] = dict2.get(c, 0) + 1

    return dict1 == dict2

assert is_permutation('abc', 'abc')
assert is_permutation('abc', 'bca')
assert is_permutation('', '')
assert not is_permutation('abc', 'abb')
assert not is_permutation('abc', 'acba')

assert is_permutation2('abc', 'abc')
assert is_permutation2('abc', 'bca')
assert is_permutation2('', '')
assert not is_permutation2('abc', 'abb')
assert not is_permutation2('abc', 'acba')

    
