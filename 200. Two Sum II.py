class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) - 1
        while lp < rp:
            if target == numbers[lp] + numbers[rp]:
                return [lp + 1, rp + 1]
            elif target > numbers[lp] + numbers[rp]:
                lp += 1
            else:
                rp -= 1