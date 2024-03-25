class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        a = sorted(stones)
        n = len(stones)
        maxMoves = max(a[n - 1] - a[1] - n + 2, a[n - 2] - a[0] - n + 2)
        minMoves = n
        start = 0
        for end in range(n):
            while a[end] - a[start] + 1 > n:
                start += 1

            if end - start + 1 == n - 1 and a[end] - a[start] + 1 == n - 1:
                minMoves = min(minMoves, 2)
            else:
                minMoves = min(minMoves, n - (end - start + 1))

        return [minMoves, maxMoves]