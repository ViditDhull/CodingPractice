class Solution:
    def minimumLength(self, s: str) -> int:
        fd = {}
        for i in s:
            fd[i] = fd.get(i, 0) + 1
        res = 0
        for char, freq in fd.items():
            if freq < 3:
                res += freq
            else:
                if freq % 2 == 0:
                    res += 2
                else:
                    res += 1
        return res
