class Solution:
    def longestMountain(self, A: List[int]) -> int:
        max_len = 0
        iterator = 1

        while iterator < len(A):
            if A[iterator] <= A[iterator - 1]:
                iterator += 1
                continue

            cur_length = 1
            while iterator < len(A) and A[iterator] > A[iterator - 1]:
                iterator += 1
                cur_length += 1

            is_mountain = False
            while iterator < len(A) and A[iterator] < A[iterator - 1]:
                is_mountain = True
                cur_length += 1
                iterator += 1

            if is_mountain:
                max_len = max(max_len, cur_length)

        return max_len