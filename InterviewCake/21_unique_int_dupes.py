#!/usr/bin/env python

def get_uniq(arr):
    return reduce(lambda x, y: x ^ y, arr, 0)
