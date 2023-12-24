class Solution(object):
    def imageSmoother(self, img):
        new_arr = []
        for i in range(len(img)):
            er = []
            for j in range(len(img[i])):
                s = 0
                n = 0
                s += img[i][j]
                n += 1
                if i > 0:
                    s += img[i-1][j]
                    n += 1
                if j > 0:
                    s += img[i][j-1]
                    n += 1
                if i < len(img) - 1:
                    s += img[i+1][j]
                    n += 1
                if j < len(img[i]) - 1:
                    s += img[i][j+1]
                    n += 1
                if i > 0 and j > 0:
                    s += img[i-1][j-1]
                    n += 1
                if i < len(img) - 1 and j < len(img[i]) - 1:
                    s += img[i+1][j+1]
                    n += 1
                if i > 0 and j < len(img[i]) - 1:
                    s += img[i-1][j+1]
                    n += 1
                if j > 0 and i < len(img) - 1:
                    s += img[i+1][j-1]
                    n += 1
                er.append(s//n)
            new_arr.append(er)
        return new_arr