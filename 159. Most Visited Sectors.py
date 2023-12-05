class Solution(object):
    def mostVisited(self, n, rounds):
        lastval = rounds[len(rounds) - 1]
        startval = rounds[0]

        if lastval > startval:
            return [i for i in range(startval, lastval + 1)]
        elif lastval == startval:
            return [startval]
        elif lastval < startval:
            res = [i for i in range(1, lastval + 1)]
            res += [i for i in range(startval, n+1)]
            return res
        else:
            return -1