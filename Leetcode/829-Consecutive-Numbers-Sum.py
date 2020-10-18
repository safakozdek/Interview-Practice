class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        if N <= 2:
            return 1

        res = 1  # self

        for i in range(2, int(sqrt(2 * N)) + 1):
            if i % 2 == 1 and N % i == 0 and i // 2 < N / i:
                res += 1
            if i % 2 == 0 and N % i == i / 2 and i // 2 < N / i:
                res += 1

        return res
