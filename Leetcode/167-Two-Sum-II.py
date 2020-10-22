class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers) - 1

        while high > low:
            current = numbers[high] + numbers[low]
            if current == target:
                return [low + 1, high + 1]
            elif current > target:
                high -= 1
            else:
                low += 1

        return []
