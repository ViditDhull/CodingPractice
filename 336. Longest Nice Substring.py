class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def isNice(string):
            for i in string:
                if i.lower() not in string or i.upper() not in string:
                    return False
            return True

        ms = ''
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if isNice(s[i:j+1]):
                    if len(s[i:j+1]) > len(ms):
                        ms = s[i:j+1]
        
        return ms
