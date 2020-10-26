class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        sPtr = 0

        for letter in t:
            if letter == s[sPtr]:
                sPtr += 1

            if sPtr == len(s):
                return True

        return False
