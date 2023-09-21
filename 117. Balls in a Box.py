class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = dict()
        for i in range(lowLimit, highLimit + 1):
            sum_dig = 0
            for digit in str(i): 
                sum_dig += int(digit)
            if sum_dig in d:
                d[sum_dig] += 1
            else:
                d[sum_dig] = 1
        return max(d.values())