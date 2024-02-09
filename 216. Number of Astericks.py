class Solution:
    def countAsterisks(self, s: str) -> int:
        pairOn = False
        count = 0
        for i in s:
            if not(pairOn):
                if i == '*':
                    count += 1
            if i == '|' and not(pairOn):
                pairOn = True
            elif i == '|' and pairOn:
                pairOn = False
        return count