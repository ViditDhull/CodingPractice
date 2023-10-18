class Solution(object):
    def search(self, nums, target):
        s_ind = 0
        e_ind = len(nums)
        while s_ind < e_ind:
            mid = (s_ind + e_ind) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                e_ind = mid
            else:
                s_ind = mid + 1
        return -1