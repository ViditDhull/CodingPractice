class Solution(object):
    def leftRightDifference(self, nums):
        asum = sum(nums)
        result = []
        lsum = 0
        rsum = asum - nums[0]
        for i in range(len(nums) - 1):
            result.append(abs(lsum - rsum))
            lsum += nums[i]
            rsum -= nums[i+1]
        result.append(asum-nums[-1])
        return result