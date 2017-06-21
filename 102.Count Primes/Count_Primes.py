class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        primes = [True] * n

        primes[0] = primes[1] = False
        for base in xrange(2, int((n - 1) ** 0.5) + 1):
            if primes[base]:
                primes[base ** 2::base] = [False] * \
                    len(primes[base ** 2::base])
        return sum(primes)
