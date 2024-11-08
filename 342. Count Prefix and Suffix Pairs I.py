class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPreSuf(str1, str2):
            if len(str1) > len(str2):
                return False
            if str1 == str2:
                return True
            j = 0
            while j < len(str1):
                if str1[j] != str2[j]:
                    return False
                j += 1

            index = -1
            for i in range(len(str1)):
                if str1[index] != str2[index]:
                    return False
                index -= 1
            return True

        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPreSuf(words[i], words[j]):
                    count += 1
        return count
