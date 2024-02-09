class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dp1 = {}

        for i in words1:
            if i in dp1:
                dp1[i] += 1
            else:
                dp1[i] = 1
        
        dp2 = {}
        for i in words2:
            if i in dp2:
                dp2[i] += 1
            else:
                dp2[i] = 1
        count = 0
        for i in words1:
            if i in dp2:
                if dp1[i] == 1 and dp2[i] == 1:
                    count += 1
        return count