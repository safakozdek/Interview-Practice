class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        left = 0
        right = len(s) - 1
        while left < right:

            while s[left] not in vowels and left < right:
                left += 1
            while s[right] not in vowels and right > left:
                right -= 1

            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            right -= 1
            left += 1

        return "".join(s)
