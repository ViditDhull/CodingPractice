class Solution:
    def countSubstrings(self, s: str) -> int:
        palindromes = 0

        for i in range(len(s)):

            lp, rp = i, i
            while lp >= 0 and rp < len(s):
                if s[lp] == s[rp]:
                    palindromes += 1
                    rp += 1
                    lp -= 1
                else:
                    break

            lp, rp = i, i + 1
            while lp >= 0 and rp < len(s):
                if s[lp] == s[rp]:
                    palindromes += 1
                    rp += 1
                    lp -= 1
                else:
                    break
            
        return palindromes