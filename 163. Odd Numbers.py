class Solution(object):
    def countOdds(self, low, high):
        if low % 2 == 0 and high % 2 == 0:
            return (high-low) / 2
        elif low % 2 != 0 and high % 2 != 0:
            return ((high-low+2) / 2)
        else:
            return (high - low + 1) // 2