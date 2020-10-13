class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        for d in path:
            if d == "." or d == "":
                pass
            elif d == "..":
                if len(stack):
                    stack.pop()
            else:
                stack.append(d)

        res = "/"

        for a in stack:
            res = res + a + "/"

        if len(res) > 1:
            res = res[:-1]

        return res
