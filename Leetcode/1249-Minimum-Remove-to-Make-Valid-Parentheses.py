class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        opens = 0
        for count in range(len(s)):

            if s[count] == "(":
                opens += 1
            elif s[count] == ")":
                if opens == 0:
                    s[count] = ""
                    continue
                opens -= 1

        closed = 0
        for count in range(len(s) - 1, -1, -1):
            if s[count] == ")":
                closed += 1
            elif s[count] == "(":
                if closed == 0:
                    s[count] = ""
                    continue
                closed -= 1

        return "".join(s)
