class Solution(object):
    def distinctAverages(self, nums):
        result = {}
        while len(nums) > 1:
            mini = min(nums)
            maxi = max(nums)
            result[float(mini+maxi) / 2] = 0
            nums.remove(mini)
            nums.remove(maxi)
        return len(result.keys())