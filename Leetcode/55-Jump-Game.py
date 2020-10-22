class Solution:
    def canJump(self, nums: List[int]) -> bool:

        maxDist = 0

        for i in range(len(nums)):
            maxDist = max(maxDist, nums[i])

            if len(nums) - i - 1 <= maxDist:
                return True

            if maxDist == 0:
                return False

            maxDist -= 1

        return False
