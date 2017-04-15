def convertToTitle(self, n):
    """
    :type n: int
    :rtype: str
    """
    res, caps = '', [chr(i + 65) for i in xrange(26)]
    while n:
        n, rem = divmod(n - 1, 26)
        res = caps[rem] + res
    return res
