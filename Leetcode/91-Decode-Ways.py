class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        last = s[0]

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            if last != "0" and int(last + s[i - 1]) <= 26:
                dp[i] += dp[i - 2]

            last = s[i - 1]

        return dp[len(s)]
