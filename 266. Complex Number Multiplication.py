class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1_split = num1.split('+')
        num2_split = num2.split('+')
        
        r1 = int(num1_split[0])
        r2 = int(num2_split[0])

        i1 = int(num1_split[1][:-1])
        i2 = int(num2_split[1][:-1])
        
        res_r = (r1 * r2) - (i1 * i2)
        res_i = (r1 * i2) + (r2 * i1)

        return str(res_r) + '+'+ str(res_i) + 'i'