class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m = len(words[0])
        n = len(target)
        count = [[0] * 26 for _ in range(m)]

        for word in words:
             for i, char in enumerate(word):
                count[i][ord(char) - ord('a')] += 1

        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for j in range(m + 1):p
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                dp[i][j] = dp[i][j - 1]
                char_index = ord(target[i - 1]) - ord('a')
                dp[i][j] = (dp[i][j] + (dp[i - 1][j - 1] * count[j - 1][char_index]) % MOD) % MOD
        return dp[n][m]
