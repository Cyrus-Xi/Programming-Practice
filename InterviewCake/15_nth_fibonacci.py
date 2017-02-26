#!/usr/bin/env python

def fib_rec(n, memo=None):
    if not memo: memo = [0, 1]
    # fib number already cached
    if n < len(memo): return memo[n]
    else:
        f = fib_rec(n-2, memo) + fib_rec(n-1, memo)
        memo.append(f)
        return f

def fib(n):
    if n in [0, 1]: return n
    prevprev, prev = 0, 1
    for i in xrange(n-1):
        f = prevprev + prev
        prevprev, prev = prev, f
    return f

print fib(8), fib_rec(8)
print fib(1), fib_rec(1)
