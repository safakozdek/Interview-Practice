class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0  # Short input

        left_break_point = None
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                left_break_point = i
                break

        if left_break_point is None:
            return 0  # Sorted case

        min_at_rest = 99999999999  # very high value (max int)
        for i in range(left_break_point, len(nums)):
            min_at_rest = min(min_at_rest, nums[i])

        left_boundary = None
        for i in range(len(nums)):
            if min_at_rest < nums[i]:
                left_boundary = i
                break

        right_break_point = None
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] < nums[i - 1]:
                right_break_point = i
                break

        max_at_rest = -999999999999
        for i in range(right_break_point):
            max_at_rest = max(max_at_rest, nums[i])

        right_boundary = None
        for i in range(len(nums) - 1, 0, -1):
            if max_at_rest > nums[i]:
                right_boundary = len(nums) - i - 1
                break

        return len(nums) - left_boundary - right_boundary
