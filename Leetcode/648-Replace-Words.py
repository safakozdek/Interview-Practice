class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = [None] * 26


class Solution:
    def convertDictToTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            cur_node = root
            for char in word:
                index = ord(char) - ord('a')

                if not cur_node.children[index]:
                    cur_node.children[index] = TrieNode()
                cur_node = cur_node.children[index]
            cur_node.is_word = True
        return root

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = self.convertDictToTrie(dictionary)
        new_sentence = []
        words = sentence.split()

        for word in words:
            cur_node = root
            for i, char in enumerate(word):
                index = ord(char) - ord('a')
                if cur_node.is_word:
                    new_sentence.append(word[:i])
                    break
                if not cur_node.children[index]:
                    new_sentence.append(word)
                    break
                cur_node = cur_node.children[index]
            else:
                new_sentence.append(word)

        return ' '.join(new_sentence)