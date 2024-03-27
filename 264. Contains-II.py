class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        nf = {}

        for i in range(len(nums)):
            if nums[i] not in nf:
                nf[nums[i]] = i
            else:
                if abs(i - nf[nums[i]]) <= k:
                    return True
                nf[nums[i]] = i
        return False