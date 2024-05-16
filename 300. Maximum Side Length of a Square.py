class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if min(min(line) for line in mat) > threshold:
            return 0

        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n + 1)]
        for line in mat:
            dp_line = [0]
            for j, elem in enumerate(line, 1):
                current = (
                    elem
                    + dp_line[-1]
                    + dp[-1][j]
                    - dp[-1][j - 1]
                )
                dp_line.append(current)
            dp.append(dp_line)
        
        def check(middle):
            for i in range(middle, m + 1):
                for j in range(middle, n + 1):
                    current = (
                        dp[i][j]
                        - dp[i - middle][j]
                        - dp[i][j - middle]
                        + dp[i - middle][j - middle]
                    )
                    if current <= threshold:
                        return True
            return False

        l = 1
        r = min(m, n)
        if check(r):
            return r

        while r - l > 1:
            middle = (l + r) // 2
            if check(middle):
                l = middle
            else:
                r = middle
        return l
