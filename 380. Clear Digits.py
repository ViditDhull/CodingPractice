class Solution:
    def clearDigits(self, s: str) -> str:
        mdi = {}
        for i in range(len(s)):
            if s[i].isdigit():
                mdi[i] = 1
                index = i
                while index in mdi and index >= 0:
                    index -= 1
                mdi[index] = 1
        res = ''
        for i in range(len(s)):
            if i not in mdi:
                res+= s[i]
        return res
