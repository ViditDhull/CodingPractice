class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sa = sentence.split()
        if sa[0][0] != sa[-1][-1]:
            return False
        for i in range(len(sa) - 1):
            if sa[i][-1] != sa[i+1][0]:
                return False
        return True