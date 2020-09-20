class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        if not A or len(A) == 0:
            return 0
        mods = dict()
        prefix_sum = [A[0] % K]
        for i in range(1, len(A)):
            prefix_sum.append((prefix_sum[-1] + A[i]) % K)

        mods[0] = 1
        result = 0
        for i in prefix_sum:
            apperance = mods.get(i, 0)
            result += apperance
            mods[i] = apperance + 1

        return result
