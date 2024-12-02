class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sl = sentence.split(' ')
        for i in range(len(sl)):
            if len(searchWord) > len(sl[i]):
                continue
            else:
                if searchWord == sl[i][:len(searchWord)]:
                    return i + 1
        return -1
