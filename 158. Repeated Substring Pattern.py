class Solution(object):
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for length in range(1, n // 2 + 1):
            if n % length == 0:
                is_repeated = True
                for i in range(length, n):
                    if s[i] != s[i - length]:
                        is_repeated = False
                        break
                if is_repeated:
                    return True
        
        return False