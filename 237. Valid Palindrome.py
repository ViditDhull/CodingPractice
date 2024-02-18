class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp, rp = 0, len(s) - 1
        while lp < rp:
            if not(s[lp].isalnum()):
                lp += 1
                continue
            if not(s[rp].isalnum()):
                rp -= 1
                continue
            
            if s[lp].lower() != s[rp].lower():
                print(s[lp], s[rp])
                return False
            lp += 1
            rp -= 1
        return True