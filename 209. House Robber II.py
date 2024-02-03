class Solution:
    def rob(self, nums: List[int]) -> int:
        a, b = 0, 0
        ln = len(nums)
        if ln == 1:
            return nums[0]
        for i in nums[:ln-1]:
            temp = max(a + i, b)
            a = b
            b = temp
        
        c, d = 0, 0
        for j in nums[1:]:
            temp = max(c + j, d)
            c = d
            d = temp
        
        return max(b,d)