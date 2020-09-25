class Solution:
    # recursive
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        cache = [-1] * (n + 1)
        cache[1], cache[2] = 1, 2

        def climb(n):
            if cache[n] > 0:
                return cache[n]
            cache[n] = climb(n - 1) + climb(n - 2)

            return cache[n]

        return climb(n)

        # dp
        def climbStairs2(self, n: int) -> int:
            if n == 1:
                return 1

            dp = [None] * (n + 1)
            dp[1] = 1
            dp[2] = 2

            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]

            return dp[n]
