class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # reverse iteration
        s_pointer = len(S) - 1
        t_pointer = len(T) - 1
        backspace_count_s = 0
        backspace_count_t = 0

        while s_pointer >= 0 or t_pointer >= 0:

            while s_pointer >= 0:
                if S[s_pointer] == '#':
                    backspace_count_s += 1
                elif S[s_pointer] != '#' and backspace_count_s > 0:
                    backspace_count_s -= 1
                else:
                    break
                s_pointer -= 1

            while t_pointer >= 0:
                if T[t_pointer] == '#':
                    backspace_count_t += 1
                elif T[t_pointer] != '#' and backspace_count_t > 0:
                    backspace_count_t -= 1
                else:
                    break
                t_pointer -= 1

            if (t_pointer < 0 and s_pointer >= 0) or (s_pointer < 0 and t_pointer >= 0):
                return False
            if (s_pointer >= 0 and t_pointer >= 0) and S[s_pointer] != T[t_pointer]:
                return False

            s_pointer -= 1
            t_pointer -= 1

        return True
