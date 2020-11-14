class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_index = bisect_left(nums, target)
        right_index = bisect_right(nums, target)

        if left_index == right_index:
            return [-1, -1]

        return [left_index, right_index - 1]