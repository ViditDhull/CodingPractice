class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        right, moves = 0, 0
        for i, f in enumerate(flips, 1):
            right = max(right, f)
            moves += right == i
        return moves
