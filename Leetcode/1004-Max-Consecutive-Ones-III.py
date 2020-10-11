class Solution:
    def longestOnes(self, A: List[int], k: int) -> int:
        max_dist = 0
        right = 0
        left = 0
        free = k
        for right in range(len(A)):
            if A[right] == 1:
                if right - left + 1 > max_dist:
                    max_dist = right - left + 1
                continue

            if free > 0:
                free -= 1
                if right - left + 1 > max_dist:
                    max_dist = right - left + 1
                continue

            while A[left] == 1:
                left += 1

            left += 1

        return max_dist
