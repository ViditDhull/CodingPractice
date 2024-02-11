class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0
        for n in numSet:
            if (n-1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength