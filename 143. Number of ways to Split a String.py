class Solution(object):
    def numWays(self, s):
        n = len(s)
        ss = s.split('1')
        ones = len(ss) - 1

        if ones % 3 != 0:
            return 0

        if ones == 0:
            return ((n-1) * (n-2)//2) % (10**9 + 7)
        
        return ((len(ss[ones//3]) + 1) * (len(ss[ones//3*2]) + 1)) % (10**9+7)