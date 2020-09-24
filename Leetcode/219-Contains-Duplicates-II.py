class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k < 1 or len(nums) == 0:
            return False
        hset = set()
        for i in range(min(k, len(nums))):
            if nums[i] in hset:
                return True
            hset.add(nums[i])

        if k > len(nums):
            return False

        for i in range(k, len(nums)):
            if nums[i] in hset:
                return True
            hset.add(nums[i])
            hset.discard(nums[i - k])  # .remove() throws KeyError

        return False
