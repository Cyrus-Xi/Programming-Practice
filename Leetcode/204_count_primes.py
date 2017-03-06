#!/usr/bin/env

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n <= 2: return 0
        
        primes = [True] * n
        primes[:2] = [False, False]
        
        for i in xrange(2, n):
            if primes[i]:
                for j in xrange(i, (n-1) / i + 1):
                    primes[i*j] = False
                    
        return sum(primes)
