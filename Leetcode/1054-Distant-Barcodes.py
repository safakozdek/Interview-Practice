class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        nums = dict()

        for i in barcodes:
            if nums.get(i, 0):
                nums[i] += 1
            else:
                nums[i] = 1

        res = [-1] * len(barcodes)
        odd = 1
        even = 0
        mostFreq = min(nums.items(), key=lambda x: -x[1])

        for i in range(mostFreq[1]):
            res[even] = mostFreq[0]
            even += 2

        for k, v in nums.items():
            if k == mostFreq[0]:
                continue

            for i in range(v):
                if even < len(barcodes):
                    res[even] = k
                    even += 2
                else:
                    res[odd] = k
                    odd += 2

        return res
