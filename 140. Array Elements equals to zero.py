class Solution(object):
    def checkArray(self, nums, k):
        cur = 0
        for i, a in enumerate(nums):
            if cur>a:
                return False
            nums[i], cur = a - cur, a
            if i >= k - 1:
                cur -= nums[i-k+1]
        return cur == 0