#!/usr/bin/env python

def compress(astr):
    # Edge cases, plus return original if compressed will not be shorter.
    if len(astr) < 3: return astr

    c_astr = ''
    # Index of compressed string.
    c_astr_i = 0
    last_char = ''
    last_char_freq = 1

    for i, c in enumerate(astr):
        if not i: 
            last_char = c
            continue
            
        if c != last_char:
            c_astr += last_char + str(last_char_freq)
            last_char = c
            last_char_freq = 1
        else:
            last_char_freq += 1

    c_astr += last_char + str(last_char_freq)

    if len(c_astr) < len(astr): return c_astr
    else: return astr
        
# "aabccccaaa" -> "a2b1c4a3"
# i = 0, last_char = a, freq = 1; freq = 2; c_astr = 'a2', last_char = b, freq = 1
# c_astr = 'a2b1', last_char = c, freq = 1; freq = 2; freq = 3; freq = 4; a_str = 'a2b1c4', last_char = a, freq = 1
# freq = 2; freq = 3
# "abbc"

assert compress('aabccccaaa') == 'a2b1c4a3'
assert compress('abbbbbc') == 'a1b5c1'
assert compress('abcd') == 'abcd'
assert compress('a') == 'a'

