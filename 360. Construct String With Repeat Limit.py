class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        fd = {}
        for i in s:
            if i not in fd:
                fd[i] = 1
            else:
                fd[i] += 1
        
        sl = sorted(list(s), reverse = True)
        distinct = []
        for i in sl:
            if i not in distinct:
                distinct.append(i)

        res = ''
        while 0 < len(distinct):
            if fd[distinct[0]] > 0:
                    if fd[distinct[0]] <= repeatLimit:
                        res += distinct[0] * fd[distinct[0]]
                        fd[distinct[0]] = 0
                        distinct.pop(0)
                    else:
                        res += distinct[0] * repeatLimit
                        fd[distinct[0]] -= repeatLimit
                        if len(distinct) > 1:
                            res += distinct[1]
                            fd[distinct[1]] -= 1
                            if fd[distinct[1]] == 0:
                                distinct.pop(1)
                        else:
                            distinct.pop(0)
            else:
                distinct.pop(0)
        return res
