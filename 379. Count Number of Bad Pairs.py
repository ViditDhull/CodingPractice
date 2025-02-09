class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_count = {}
        bad_pairs = 0
        for pos in range(n):
            diff = pos - nums[pos]

            good_pairs_count = diff_count.get(diff, 0)

            bad_pairs += pos - good_pairs_count
            
            diff_count[diff] = good_pairs_count + 1
        return bad_pairs
