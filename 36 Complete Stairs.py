class Solution(object):
    def arrangeCoins(self, n):
        completedStairs = 0
        k = 1
        
        while n >= 0:
            n -= k
            if n >= 0:
                completedStairs += 1
            k += 1
        return completedStairs