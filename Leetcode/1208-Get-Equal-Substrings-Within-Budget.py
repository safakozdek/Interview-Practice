class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        budget = maxCost
        left = 0
        maxlength = 0
        for right in range(len(s)):
            cost = abs(ord(s[right]) - ord(t[right]))

            if cost <= budget:
                budget -= cost
                if right - left + 1 > maxlength:
                    maxlength = right - left + 1
            else:
                while right > left and cost > budget:
                    cost_left = abs(ord(s[left]) - ord(t[left]))
                    budget += cost_left
                    left += 1

                if cost > budget:
                    left += 1
                else:
                    budget -= cost

        return maxlength
