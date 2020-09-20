class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(prefix_sum[-1] + num)

        prefix_sum.pop(0)
        d = dict()
        d[0] = 1
        result = 0
        for i in prefix_sum:
            complements = d.get(i - k, 0)
            result += complements
            d[i] = d.get(i, 0) + 1

        return result