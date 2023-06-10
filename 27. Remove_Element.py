class Solution(object):
    def removeElement(self, nums, val):
        nums [:]= [i for i in nums if i != val]
        return len(nums)