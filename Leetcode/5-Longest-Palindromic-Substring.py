class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        start = 0
        for i in range(2 * len(s) - 1):
            mid = i // 2
            curHalfLen = 1
            curStart = 0
            final_len = 0

            if i % 2 == 0:  # odd length
                while mid - curHalfLen >= 0 and mid + curHalfLen < len(s):
                    if s[mid - curHalfLen] != s[mid + curHalfLen]:
                        break
                    else:
                        curStart = mid - curHalfLen
                        curHalfLen += 1

                final_len = curHalfLen * 2 - 1

            elif s[mid] == s[mid + 1]:  # even length
                curStart = mid

                while mid - curHalfLen >= 0 and mid + curHalfLen + 1 < len(s):
                    if s[mid - curHalfLen] != s[mid + curHalfLen + 1]:
                        break
                    else:
                        curStart = mid - curHalfLen
                        curHalfLen += 1

                final_len = curHalfLen * 2

            if final_len > maxLen:  # check final length
                start = curStart
                maxLen = final_len

        return s[start:start + maxLen]
