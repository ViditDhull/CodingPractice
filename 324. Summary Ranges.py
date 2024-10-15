class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        lp = 0

        result = []
        ran = ''
        while lp < len(nums) - 1:
            if len(ran) == 0:
                if nums[lp+1] - nums[lp] > 1:
                    result.append(str(nums[lp]))
                else:
                    ran += str(nums[lp]) + '->'
            else:
                if nums[lp+1] - nums[lp] > 1:
                    result.append(ran + str(nums[lp]))
                    ran = ''
            lp += 1
        
        if len(ran) == 0:
            result.append(str(nums[-1]))
        else:
            ran += str(nums[-1])
            result.append(ran)

        return result
