class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        else:
            primes = [True] * n
            primes[:2] = [False, False]
            for num in range(2, int(n ** 0.5) + 1):
                primes[num ** 2:n:num] = [False] * len(primes[num ** 2:n:num])
        return print(sum(primes))

solution = Solution()
solution.countPrimes(100)
