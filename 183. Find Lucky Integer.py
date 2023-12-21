class Solution(object):
    def findLucky(self, arr):
        frq = {}
        for i in arr:
            if i in frq:
                frq[i] += 1
            else:
                frq[i] = 1
        result = []
        for i in frq.keys():
            if frq[i] == i:
                result.append(i)
        if len(result) == 0:
            return -1
        else:        
            result.sort()
            return result[-1]
