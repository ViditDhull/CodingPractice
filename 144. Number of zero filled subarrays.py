class Solution(object):
    def zeroFilledSubarray(self, nums):
        app = 0
        res = 0
        for i in nums:
            if i == 0:
                app += 1
                res += app
            else:
                app = 0
        return res