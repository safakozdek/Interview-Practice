class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()

        for char in s:
            if hashmap.get(char):
                hashmap[char] += 1
            else:
                hashmap[char] = 1

        for i in range(len(s)):
            if hashmap[s[i]] == 1:
                return i

        return -1