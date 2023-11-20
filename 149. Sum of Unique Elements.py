class Solution(object):
    def sumOfUnique(self, nums):
        num_sum = 0
        for i in nums:
            if nums.count(i) == 1:
                num_sum += i
        return num_sum