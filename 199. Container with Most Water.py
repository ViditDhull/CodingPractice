class Solution:
    def maxArea(self, height: List[int]) -> int:
        lp = 0
        rp = len(height) - 1
        max_area = 0
        while rp > lp:
            max_area = max((rp-lp) * min(height[lp], height[rp]), max_area)
            if height[lp] > height[rp]:
                rp -= 1
            else:
                lp += 1
        return max_area