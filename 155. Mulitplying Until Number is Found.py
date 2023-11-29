class Solution(object):
    def findFinalValue(self, nums, original):
        if original in nums:
            return self.findFinalValue(nums, original * 2)
        else:
            return original