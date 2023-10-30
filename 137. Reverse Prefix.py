class Solution(object):
    def reversePrefix(self, word, ch):
        if ch not in word:
            return word
        index = word.index(ch)
        rever_word =  word[:index + 1]
        return rever_word[::-1] + word[index + 1:]