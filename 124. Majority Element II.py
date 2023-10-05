class Solution(object):
    def majorityElement(self, nums):
        n_occ = int(len(nums)/3)
        result = set()
        for i in nums:
            if nums.count(i) > n_occ:
                result.add(i)
        return result