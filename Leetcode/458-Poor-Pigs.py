class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        max_obs = minutesToTest // minutesToDie
        return ceil(log(buckets, max_obs + 1))
