class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_rn = {}
        for i in ransomNote:
            if i in count_rn:
                count_rn[i] += 1
            else:
                count_rn[i] = 1

        count_mg = {}
        for i in magazine:
            if i in count_mg:
                count_mg[i] += 1
            else:
                count_mg[i] = 1
                
        for i in count_rn:
            if i not in count_mg:
                return False
            else:
                if count_rn[i] > count_mg[i]:
                    return False
        return True
