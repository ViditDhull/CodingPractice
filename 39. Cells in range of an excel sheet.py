class Solution(object):
    def titleToNumber(self, columnTitle):
        s = 0
        for jj in columnTitle:
            s = s * 26 + ord(jj) - ord('A') + 1
        return s