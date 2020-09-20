import re


class Solution:
    def mostCommonWord(self, s: str, banned: List[str]) -> str:
        s = re.sub(r'[^\w\s]', ' ', s).lower()
        s = s.split(" ")
        banned = set(banned)
        word_frequencies = dict()

        for word in s:
            if word not in banned and len(word) > 0:
                freq = word_frequencies.get(word, 0)
                word_frequencies[word] = freq + 1

        max_word = None
        max_count = 0
        for k, v in word_frequencies.items():
            if v > max_count:
                max_word = k
                max_count = v

        return max_word
