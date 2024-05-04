class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        n = sum(nums)
        nDiv = n % 3
        if nDiv == 0:
            return n
        terms = [0] + sorted(filter(lambda x: x % 3 != 0, nums))[:4]

        return n - min(map(sum, filter(lambda x: (x[0] + x[1]) % 3 == nDiv, combinations(terms, 2))))