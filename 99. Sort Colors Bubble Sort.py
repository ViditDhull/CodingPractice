class Solution(object):
    def sortColors(self, nums):
        size = len(nums)
        for j in range(len(nums) - 1):
            for i in range(len(nums) - 1 -j):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = nums[i+1]
                    nums[i+1] = temp

        return nums