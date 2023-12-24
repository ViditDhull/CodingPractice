class Solution(object):
    def findLHS(self, nums):
        fd = {}
        for i in nums:
            if i not in fd:
                fd[i] = 1
            else:
                fd[i] += 1
        mfs = 0
        ka = sorted(fd.keys())
        for i in range(len(ka)-1):
            if abs(ka[i] - ka[i+1]) == 1:
                if mfs < fd[ka[i]] + fd[ka[i+1]]:
                    mfs = fd[ka[i]] + fd[ka[i+1]]
        return mfs