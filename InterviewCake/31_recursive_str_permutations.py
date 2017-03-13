#!/usr/bin/env python

def gen_permutes(s):
    if len(s) < 2: return set([s])
    new_perms = gen_permutes(s[1:])
    perms = set()
    for p in new_perms:
        # Add the first character at each position in the permutation.
        for i in xrange(len(p) + 1):
            new_p = p[:i] + s[0] + p[i:]
            perms.add(new_p)
    return perms
                         
def gen_permutes2(s, st, end):
    if st == end: return set([s])
    perms, s = set(), list(s)
    for i in xrange(st, end + 1):
        s[st], s[i] = s[i], s[st]
        perms.update(gen_permutes2(''.join(s), st + 1, end))
        # Backtrack.
        s[i], s[st] = s[st], s[i]
    return perms


if __name__ == '__main__':
    from timeit import timeit

    def wrapper(func, *args, **kwargs):
        def wrapped():
            return func(*args, **kwargs)
        return wrapped

    s = 'aabfcd'
    wrapped = wrapper(gen_permutes, s)
    wrapped2 = wrapper(gen_permutes2, s, 0, 5)

    g1 = round(timeit(wrapped, number=10000), 3)
    print 'gen_permutes of {} took {} seconds to get:'.format(s, str(g1))
    print gen_permutes('aabcd')

    print
    g2 = round(timeit(wrapped2, number=10000) * 1000, 3)
    print 'gen_permutes2 of {} took {} seconds to get:'.format(s, str(g1))
    print gen_permutes2('aabcd', 0, 4)


