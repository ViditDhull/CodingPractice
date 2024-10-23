class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if n == 1 and k != 0:
            return code
        res = [0] * n
        if k == 0:
            return [0] * n
        elif k > 0:
            for i in range(n):
                if i + k < n:
                    res[i] = sum(code[i+1:i+k+1])
                else:
                    res[i] = sum(code[i+1:n]) + sum(code[:(k - (n - i - 1))])
        else:
            k = abs(k)
            for i in range(n):
                if i - k > 0:
                    res[i] = sum(code[i-k: i])
                else:
                    res[i] = sum(code[:i]) + sum(code[n - (k - i):n])
        return res
