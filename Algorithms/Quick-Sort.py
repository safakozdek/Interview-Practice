def quickSort(arr):
    quickSortHelper(arr, 0, len(arr) - 1)


def quickSortHelper(arr, low, high):
    if high < low:
        return arr

    p = partition(arr, low, high)
    quickSortHelper(arr, low, p - 1)
    quickSortHelper(arr, p + 1, high)


def get_pivot(arr, low, high):
    # Median of three
    mid = (low + high) // 2

    if arr[low] < arr[mid]:
        if arr[mid] < arr[high]:
            return mid
    elif arr[low] < arr[high]:
        return low

    return high


def partition(arr, low, high):
    pivotIndex = get_pivot(arr, low, high)
    pivotValue = arr[pivotIndex]
    arr[pivotIndex], arr[low] = arr[low], arr[pivotIndex]
    border = low

    for i in range(low, high + 1):
        if arr[i] < pivotValue:
            border += 1
            arr[i], arr[border] = arr[border], arr[i]

    arr[low], arr[border] = arr[border], arr[low]
    return border


if __name__ == "__main__":
    nums = [4, 6, 7, 2, 9, 12, 1, 4, 2, 5, 3, 0, -5, 8]
    quickSort(nums)
    print(nums)
