class Solution(object):
    def diagonalPrime(self, nums):
        def isPrime(n):
            for i in range(2, int(sqrt(n)) + 1):
                if n % i == 0: return False
            return n > 1
        
        res, L = 0, len(nums)
        for i in range(L):
            n1, n2 = nums[i][i], nums[i][~i]
            if n1 > res and isPrime(n1): res = n1
            if n2 > res and isPrime(n2): res = n2

        return res 