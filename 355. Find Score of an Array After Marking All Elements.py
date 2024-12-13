class Solution:
    def findScore(self, nums: List[int]) -> int:
        n=len(nums)
        sum, r=0, 0
        while r<n:
            l=r
            while r+1<n and nums[r]>nums[r+1]:
                r+=1
            for i in range(r, l-1, -2):
                sum+=nums[i]
            r+=2
        return sum
        
