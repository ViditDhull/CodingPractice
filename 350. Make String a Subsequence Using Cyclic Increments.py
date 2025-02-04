class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        inc_dict = {'a':'b', 'b':'c', 'c':'d', 'd':'e', 'e':'f', 'f':'g', 'g':'h', 'h':'i', 'i':'j', 'j':'k', 'k':'l', 'l':'m', 'm':'n', 'n':'o', 'o':'p', 'p': 'q', 'q':'r', 'r':'s', 's':'t', 't':'u', 'u':'v', 'v':'w', 'w':'x', 'x':'y', 'y':'z', 'z':'a'}
        i, j = 0, 0

        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or inc_dict[str1[i]] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(str2)
