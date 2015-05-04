#!/usr/bin/env python

# Challenge description:
# Write a program which prints all the permutations of a string in alphabetical 
# order. We consider that digits < upper case letters < lower case letters. The 
# sorting should be performed in ascending order. 

import sys
import fileinput

def permute_handler(a_str):
    gen = getPermutations(a_str[:-1])
    permutations = []
    
    for combination in gen:
        permutations.append(combination)

    permutations.sort()
    print ','.join(permutations)
        
def getPermutations(string):
    if len(string) == 1:
        yield string
    else:
        for i in xrange(len(string)):
            for perm in getPermutations(string[:i] + string[i+1:]):
                yield string[i] + perm

for line in fileinput.input():
    permute_handler(line)
