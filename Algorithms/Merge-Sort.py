def mergeSort(arr):
    mergeSortHelper(arr, 0, len(arr) - 1)


def mergeSortHelper(arr, low, high):
    if high <= low:
        return

    mid = (low + high) // 2
    mergeSortHelper(arr, low, mid)
    mergeSortHelper(arr, mid + 1, high)
    merge(arr, low, mid + 1, high)
    return None


def merge(arr, low, mid, high):
    left = arr[low: mid]
    right = arr[mid: high + 1]
    lp = rp = 0
    mergeIndex = low

    while lp < len(left) and rp < len(right):
        if left[lp] < right[rp]:
            arr[mergeIndex] = left[lp]
            lp += 1
        else:
            arr[mergeIndex] = right[rp]
            rp += 1
        mergeIndex += 1

    while lp < len(left):
        arr[mergeIndex] = left[lp]
        lp += 1
        mergeIndex += 1

    while rp < len(right):
        arr[mergeIndex] = right[rp]
        rp += 1
        mergeIndex += 1

    return None


if __name__ == "__main__":
    nums = [4, 6, 7, 2, 9, 12, 1, 4, 2, 5, 3, 0, -5, 8]
    mergeSort(nums)
    print(nums)
