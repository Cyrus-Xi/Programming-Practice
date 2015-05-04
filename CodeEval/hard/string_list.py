#!/usr/bin/env python

# Challenge description:
# You are given a number N and a string S. Print all of the possible ways to write 
# a string of length N from the characters in string S, comma delimited in 
# alphabetical order.

from fileinput import input
from itertools import product

for line in [line.strip() for line in input() if line != "\n"]:
    N, letters = line.split(",")
    # Not permutations because letters can be repeated.
    words = [''.join(word) for word in list(product(letters, repeat=int(N)))]
    # Put in alphabetical order and remove duplicates.
    words = sorted(set(words))
    print(','.join(words))
