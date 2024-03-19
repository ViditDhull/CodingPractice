class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def bal_num(num):
            fd = {}
            for i in str(num):
                fd[i] = fd.get(i, 0) + 1
            for j in fd.keys():
                if int(j) != fd[j]:
                    return False
            else:
                return True
        res = n + 1
        while not bal_num(res):
            res += 1
        return res