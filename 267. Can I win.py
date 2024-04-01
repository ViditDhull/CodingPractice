class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
            return False

        @cache
        def func(nums, total):
            if any(total <= x for x in nums):
                return True
            return any(not func(nums-{x}, total - x) for x in nums)

        return func(frozenset(range(1, maxChoosableInteger + 1)), desiredTotal)