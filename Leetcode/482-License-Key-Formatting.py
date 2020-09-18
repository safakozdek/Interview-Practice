class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        result = S.upper().replace("-", "")

        if len(result) < 1:
            return ""

        mod = len(result) % K

        real_result = result[:mod]

        for i in range(mod, len(result)):
            if i % K == mod:
                real_result += "-"

            real_result += result[i]

        if real_result[0] == "-":
            return real_result[1:]

        return real_result