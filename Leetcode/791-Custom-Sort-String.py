class Solution:
    def customSortString(self, S: str, T: str) -> str:
        sortPriority = dict()

        for i in range(len(S)):
            sortPriority[S[i]] = i

        T = sorted(T, key=lambda x: (sortPriority.get(x, -1)))

        return "".join(T)
