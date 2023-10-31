class Solution(object):
    def isAnagram(self, s, t):
        if len(t) != len(s):
            return False
        s_freq = {}
        t_freq = {}
        for i in s:
            s_freq[i] = s_freq.get(i, 0) + 1
        for i in t:
            t_freq[i] = t_freq.get(i, 0) + 1

        return s_freq == t_freq