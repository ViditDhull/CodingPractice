class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        res = [''] * len(s)
        lp, rp = 0, len(s) - 1
        while lp <= rp:
            if s[lp].lower() in vowels and s[rp].lower() in vowels:
                res[lp] = s[rp]
                res[rp] = s[lp]
                lp += 1
                rp -= 1
            elif s[lp].lower() in vowels and s[rp].lower() not in vowels:
                res[rp] = s[rp]
                rp -= 1
            else:
                res[lp] = s[lp]
                lp += 1
        return ''.join(res)
