class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        for i in range(len(s)):

            lp, rp = i, i
            each = s[i]
            while lp >= 0 and rp < len(s):
                if s[lp] == s[rp]:
                    each = s[lp: rp + 1]
                    rp += 1
                    lp -= 1
                else:
                    break
            if len(each) > len(longest):
                longest = each
            
            lp, rp = i, i + 1
            while lp >= 0 and rp < len(s):
                if s[lp] == s[rp]:
                    each = s[lp: rp + 1]
                    rp += 1
                    lp -= 1
                else:
                    break
            if len(each) > len(longest):
                longest = each
            
        return longest