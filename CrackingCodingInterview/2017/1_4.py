#!/usr/bin/env python

# This isn't in-place though.
def replace_spaces(astr):
    alst = list(astr.strip())

    # Undefined if string is all spaces.
    if all(c == ' ' for c in alst): return -1

    alst = ['%20' if c == ' ' else c for c in alst]

    return ''.join(alst)

def replace_spaces2(astr):
    alst = list(astr)
    
    # Undefined if string is all spaces.
    if all(c == ' ' for c in alst): return -1

    for i, c in enumerate(alst):
        # Skip non-spaces.
        if c != ' ': continue

        # Move the elements after the space to make room for the %20.
        alst[i+3:len(alst[i+1:-2])+i+3+1] = alst[i+1:-2]
        # Replace the space with %20.
        alst[i:i+3] = ['%', '2', '0']

    return ''.join(alst)
         

# "This is a test      " -> "This%20is%20a%20test"
# "ab c  " -> "ab%20c"
# i = 2; 'c'; "ab   c"

assert replace_spaces("This is a test      ") == "This%20is%20a%20test"
assert replace_spaces("ab c  ") == "ab%20c"
assert replace_spaces("   ") == -1

assert replace_spaces2("This is a test      ") == "This%20is%20a%20test"
assert replace_spaces2("ab c  ") == "ab%20c"
assert replace_spaces2("   ") == -1
