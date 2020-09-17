class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # for each number i, mark index i-1 as negative
        # check positives, return them

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        # returned list does not count as extra space
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        return result
