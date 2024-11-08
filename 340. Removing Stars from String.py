class Solution:
    def removeStars(self, s: str) -> str:
        sl = []
        for i in range(len(s)):
            if s[i] == '*':
                sl.pop()
            else:
                sl.append(s[i])
        
        return ''.join(sl)
