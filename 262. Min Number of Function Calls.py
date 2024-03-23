class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        nums.sort()
        while(nums[-1] > 0):
            for i in range(n):
                if nums[i] % 2:
                    nums[i] -= 1
                    ans += 1
            if nums[-1] > 0:
                for i in range(n):
                    nums[i] //= 2
                ans += 1
        return ans