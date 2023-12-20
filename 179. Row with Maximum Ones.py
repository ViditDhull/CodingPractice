class Solution(object):
    def rowAndMaximumOnes(self, mat):
        drc = {}
        for i in range(len(mat)):
            drc[i] = 0
            for j in mat[i]:
                if j == 1:
                    drc[i] += 1
        
        maximum_count = max(drc.values())
        for i in drc.keys():
            if drc[i] == maximum_count:
                return [i,drc[i]]