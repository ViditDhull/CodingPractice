class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        c_max = 1
        c_min = 1
        for n in nums:
            temp_max = c_max
            c_max = max(n * c_max, n * c_min, n)
            c_min = min(n * temp_max, n * c_min, n)
            res = max(res, c_max, c_min, n)
        return res