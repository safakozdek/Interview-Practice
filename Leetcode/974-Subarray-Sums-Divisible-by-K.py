class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        mods = dict()
        prefix_sum = [0]
        for i in A:
            prefix_sum.append((prefix_sum[-1] + i) % K)

        prefix_sum.pop(0)
        mods[0] = 1
        result = 0
        for i in prefix_sum:
            apperance = mods.get(i, 0)
            result += apperance
            mods[i] = apperance + 1

        return result
