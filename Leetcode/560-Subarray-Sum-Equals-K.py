class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < 1:
            return 0

        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        d = dict()
        d[0] = 1
        result = 0
        for i in prefix_sum:
            complements = d.get(i - k, 0)
            result += complements
            d[i] = d.get(i, 0) + 1

        return result
