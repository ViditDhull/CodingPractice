class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1
        while lp <= rp:
            index = (lp + rp) // 2
            if nums[index] == target:
                return index

            if nums[lp] <= nums[index]:
                if target > nums[index] or target < nums[lp]:
                    lp = index + 1
                else:
                    rp = index - 1
            else:
                if target < nums[index] or target > nums[rp]:
                    rp = index - 1
                else:
                    lp = index + 1
        return -1