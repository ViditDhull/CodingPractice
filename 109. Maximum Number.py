class Solution:
    def findLargest(self, N, S):
        if (S == 0) :
     
            if(N == 1) :
                return 0
            else :
                return -1
        if (S > 9 * N) :
            return -1
        
        res = ['0'] * N
        
        for i in range(0, N) :
            if (S >= 9) :
                res[i] = '9'
                S = S - 9
            else :
                res[i] = str(S)
                S = 0
        return ''.join(res)