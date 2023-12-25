class Solution:
    def findGCD(self, nums: List[int]) -> int:
        s = min(nums)
        l = max(nums)
        if l % s == 0:
            return s
        else:
            for i in range(s,0,-1):
                if l % i == 0 and s % i == 0:
                    return i
            return 1