class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]
        cur_sum = sum(nums[:k])
        max_sum = cur_sum
        for i in range(k, len(nums)):
            cur_sum = cur_sum - nums[i-k] + nums[i]
            max_sum = max(max_sum,cur_sum)
        return max_sum / k
