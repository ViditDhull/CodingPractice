class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        res = []
        nc = 0
        fd = {}
        for i in range(n):
            if A[i] in fd:
                nc += 1
            else:
                fd[A[i]] = 1
            if B[i] in fd:
                nc += 1
            else:
                fd[B[i]] = 1
            res.append(nc)
        return res
