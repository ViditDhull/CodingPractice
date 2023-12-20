class Solution(object):
    def differenceOfSum(self, nums):
        els = 0
        ds = 0
        for i in nums:
            els += i
            for j in str(i):
                ds += int(j)
        return abs(els-ds)