class Solution(object):
    def orderlyQueue(self, s, k):
        if k == 1:
            n = len(s)
            ss = s + s
            lex_min_str = s
            for i in range(n):
                lex_min_str = min(lex_min_str, ss[i:i+n])
            return lex_min_str
        
        return "".join(sorted(s))