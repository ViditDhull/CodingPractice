class Solution(object):
    def diStringMatch(self, s):
        min_ap = 0
        max_ap = len(s)
        res = []
        for i in s:
          if i == 'I':
            res.append(min_ap)
            min_ap += 1
          elif i == 'D':
            res.append(max_ap)
            max_ap -= 1
        
        n = len(res)
        expected = n*(n+1)/2
        got = sum(res)
        to_add = expected - got
        res.append(to_add)
        return res