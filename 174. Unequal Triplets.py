class Solution(object):
    def unequalTriplets(self, nums):
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i,n):
                for k in range(j,n):
                    if nums[i] != nums[j] and nums[j] != nums[k] and nums[i] != nums[k]:
                        count += 1
        return count