class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        c_map = {}
        for i in range(len(s)):
            c_map[s[i]] = t[i]
        res1 = ''
        for i in range(len(s)):
            res1 += c_map[s[i]]

        c_map2 = {}
        for i in range(len(s)):
            c_map2[t[i]] = s[i]
        res2 = ''
        for i in range(len(s)):
            res2 += c_map2[t[i]]
        
        return res1 == t and res2 == s