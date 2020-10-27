class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap = dict()

        for i in range(len(s) - 9):
            if hmap.get(s[i:i + 10], 0):
                hmap[s[i:i + 10]] += 1
            else:
                hmap[s[i:i + 10]] = 1

        return [key for key, value in hmap.items() if value > 1]

    """
    Although the naive way is fast it cost a lot of extra spaces. 
    The alternative way to do this is making a integer key for the 10 letter string. 
    Although the time increased a little bit but the space reduced to sizeof(int)/(sizeof("AAAAAAAAAA")
    """
