class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] != 1:
                rp = i
                break
        else:
            rp = len(nums)
        sp = sum(nums[:rp])
        while sp in nums:
            sp += 1
        return sp
