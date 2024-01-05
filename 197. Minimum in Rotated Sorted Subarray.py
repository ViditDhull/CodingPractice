class Solution:
    def findMin(self, nums: List[int]) -> int:
        ln = len(nums)
        lp = 0
        rp = ln - 1
        res = nums[0]
        while lp <= rp:
            if nums[lp] < nums[rp]:
                res = min(nums[lp], res)
                break
            mp = (lp + rp)//2
            res = min(nums[mp], res)
            if nums[lp] <= nums[mp]:
                lp = mp + 1
            else:
                rp = mp - 1
        return res