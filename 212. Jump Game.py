class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                dp[i] = 1
            temp = 1
            while nums[i] >= temp and i + temp < len(dp):
                if dp[temp + i] == 1:
                    dp[i] = 1
                    break
                temp += 1
        return (dp[0] == 1)