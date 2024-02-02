class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        if len(nums) == 1:
            return nums[0]
        for i in nums:
            temp = max(a + i, b)
            a = b
            b = temp
        return b