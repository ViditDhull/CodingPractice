class Solution(object):
    def smallestEqual(self, nums):
        len_arr = len(nums)
        for i in range(len_arr):
            if i % 10 == nums[i]:
                return i
        return -1