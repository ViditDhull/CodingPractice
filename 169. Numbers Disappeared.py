class Solution(object):
    def findDisappearedNumbers(self, nums):
        return set(range(1,len(nums) + 1)) - set(nums)