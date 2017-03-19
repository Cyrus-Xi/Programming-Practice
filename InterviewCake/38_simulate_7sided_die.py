#!/usr/bin/env python

from random import randint

def rand5():
    return randint(1, 5)

def rand7():
    acc = 0
    for _ in xrange(7):
        acc += rand5()
    return acc % 7 + 1

def rand7_alt():
    while True:
        outcome = (rand5() - 1) * 5 + (rand5() - 1) + 1
        # Get rid of last 4 numbers, since 25 isn't divisible by 7, but 21 is.
        if outcome > 21: continue
        return outcome % 7 + 1

def driver(n, rand7_func):
    """Test if rand7 returns evenly distributed int from 1 to 7."""
    results = [0] * 7
    for _ in xrange(n):
        res = rand7_func() - 1
        results[res] += 1
    # Also return the proportion.
    return [(r, round(float(r) / sum(results), 3)) for r in results]

print driver(10000, rand7)
print driver(10000, rand7_alt)

if __name__ == '__main__':
    from timeit import Timer

    import_stmt = 'from __main__ import driver, rand5, rand7, rand7_alt;'
    setup = import_stmt + 'n = 1000; rand7_func = '

    # min recommended: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module
    rand7_time = round(min(Timer('driver(n, rand7_func)', setup=setup + 'rand7').repeat(3, 100)), 2)
    rand7_alt_time = round(min(Timer('driver(n, rand7_func)', setup=setup + 'rand7_alt').repeat(3, 100)), 2)

    print 'rand7 time: {}s'.format(rand7_time)
    print 'rand7_alt time: {}s'.format(rand7_alt_time)
