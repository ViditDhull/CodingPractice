class Solution:
    def reverseWords(self, s: str) -> str:
        if len(s) == 1:
            return s

        words_list = []
        word = ''
        lp = 0
        while lp < len(s):
            if len(word) == 0 and s[lp] == ' ':
                lp += 1
                continue
            elif len(word) != 0 and s[lp] == ' ':
                words_list.append(word)
                word = ''
            else:
                word += s[lp]
            lp += 1
        if len(word) > 0:
            words_list.append(word)
        return ' '.join(words_list[::-1])
