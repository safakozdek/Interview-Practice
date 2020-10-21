def binarySearch(nums, target):
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        num = nums[mid]

        if num == target:
            return True
        elif num < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


if __name__ == "__main__":
    listToSearch = [1, 2, 3, 6, 5, 4, 7, 0]
    listToSearch = sorted(listToSearch)

    inIt = binarySearch(listToSearch, 8)
    print("Is 8 in list? {}".format(inIt))
    inIt = binarySearch(listToSearch, 2)
    print("Is 2 in list? {}".format(inIt))
