class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        string = {}
        res = 0
        for r, c in enumerate(s):
            if c in string and string[c] >= l:
                l = string[c] + 1
            string[c] = r
            res = max(res, r - l + 1)
        return res