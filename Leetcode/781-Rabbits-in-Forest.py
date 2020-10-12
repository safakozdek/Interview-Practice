class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        hmap = dict()
        for ans in answers:
            if hmap.get(ans, 0):
                hmap[ans] += 1
            else:
                hmap[ans] = 1

        res = 0

        for k, v in hmap.items():
            excess = v % (k + 1)
            res += v
            if excess:
                res += k - excess + 1

        return res
