class Solution(object):
    def numSpecial(self, mat):
        lm = len(mat)
        csp = 0
        for i in range(lm):
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    c1 = 0
                    for m in range(lm):
                        if mat[m][j] == 1:
                            c1 += 1
                    c2 = 0
                    for n in range(len(mat[i])):
                        if mat[i][n] == 1:
                            c2 += 1
                    if c1 == 1 and c2 == 1:
                        csp += 1
        return csp