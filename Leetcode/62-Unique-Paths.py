class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * m] * n
        dp[0][0] = 1

        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]
