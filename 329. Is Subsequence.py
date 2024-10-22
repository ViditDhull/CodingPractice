class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = 0
        tp = 0

        while sp < len(s) and tp < len(t):
            if sp == len(s):
                return True
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        return sp >= len(s)