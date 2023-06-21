class Solution:
    def romanToInt(self, s: str) -> int:
    
        # rti is a dict for roman to intgers values
        rti = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        # ans is for our sum value
        ans=0

        # for loop till len(s)-1 cause for last Roman Value we cant compare
        for i in range(len(s)-1):
            if rti[s[i]] < rti[s[i+1]]:
                ans = ans - rti[s[i]]
            else:   
                ans = ans + rti[s[i]]

        # So we add the last value and return the final ans
        return ans+rti[s[-1]]