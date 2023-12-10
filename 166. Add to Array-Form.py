class Solution(object):
    def addToArrayForm(self, num, k):
        number = ''
        for i in num:
            number += str(i)
        knum = int(number) + k
        result = []
        for i in str(knum):
            result.append(int(i))
        return result