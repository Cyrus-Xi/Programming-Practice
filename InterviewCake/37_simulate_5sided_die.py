#!/usr/bin/env python

from random import randint

def rand7():
    return randint(1, 7)

def rand5():
    acc = 0
    for _ in xrange(5):
        acc += rand7()
    return acc % 5 + 1

def rand5_recursive():
    roll = rand7()
    return roll if roll <= 5 else rand5_recursive()

def driver(n, rand5_func):
    """Test if rand5 returns evenly distributed int from 1 to 5."""
    results = [0] * 5
    for _ in xrange(n):
        res = rand5_func() - 1
        results[res] += 1
    # Also return the proportion.
    return [(r, round(float(r) / sum(results), 3)) for r in results]


if __name__ == '__main__':
    rand5_res = driver(100000, rand5)
    print 'rand5 results: {}'.format(rand5_res)
    diff =  max(rand5_res, key=lambda x: x[1])[1] - min(rand5_res, key=lambda x: x[1])[1]
    print 'max proportion diff: {}'.format(diff)
    rand5_rec_res = driver(100000, rand5_recursive)
    print 'rand5_recursive results: {}'.format(rand5_rec_res)
    diff_rec = max(rand5_rec_res, key=lambda x: x[1])[1] - min(rand5_rec_res, key=lambda x: x[1])[1]
    print 'max proportion diff: {}'.format(diff_rec)

    from timeit import Timer

    import_stmt = 'from __main__ import driver, rand5, rand5_recursive, rand7;'
    setup = import_stmt + 'n = 1000; rand5_func = '

    # min recommended: http://stackoverflow.com/questions/8220801/how-to-use-timeit-module
    rand5_time = round(min(Timer('driver(n, rand5_func)', setup=setup + 'rand5').repeat(3, 100)), 2)
    rand5_rec_time = round(min(Timer('driver(n, rand5_func)', setup=setup + 'rand5_recursive').repeat(3, 100)), 2)

    print 'rand5 time: {}s'.format(rand5_time)
    print 'rand5_recursive time: {}s'.format(rand5_rec_time)
