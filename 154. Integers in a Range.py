class Solution(object):
    def isCovered(self, ranges, left, right):
        result = []
        for i in range(left, right+1):
            for j in range(len(ranges)):
                if i in range(ranges[j][0], ranges[j][1]+1):
                    result.append(0)
                    break
        return len(result) == (right-left+1)