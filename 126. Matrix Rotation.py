class Solution(object):
    def findRotation(self, mat, target):
        val = 0
        while val < 4:
            mat = [list(i) for i in zip(*mat)[::-1]]
            if mat == target:
                return True
            val += 1
        return False