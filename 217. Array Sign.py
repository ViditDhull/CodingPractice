class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if nums[0] < 0:
            sign = -1
        elif nums[0] == 0:
            sign = 0
        elif nums[0] > 0:
            sign = 1

        for i in nums[1:]:
            if sign == 0:
                break
            if i < 0:
                if sign == -1:
                    sign = 1
                elif sign == 1:
                    sign = -1
            if i == 0:
                sign = 0
                break
        return sign