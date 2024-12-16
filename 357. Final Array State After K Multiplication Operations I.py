class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            index_of_min = nums.index(min(nums))
            nums[index_of_min] = nums[index_of_min] * multiplier
        
        return nums
