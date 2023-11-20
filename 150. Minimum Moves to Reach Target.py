class Solution(object):
    def minMoves(self, target, maxDoubles):
        num = 1
        moves = 0
        while num != target:
            if maxDoubles > 0:
                if target % 2 == 0:
                    target = target / 2
                    maxDoubles -= 1
                    moves += 1
                else:
                    target -= 1
                    moves += 1
            else:
                moves += (target - num)
                num = target
        return moves