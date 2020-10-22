class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 0

        low, high = 0, len(arr) - 1

        while high >= low:
            mid = (high + low) // 2

            if mid == len(arr) - 1 and arr[mid] > arr[mid - 1]:
                return mid
            elif arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid + 1] > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return 0
