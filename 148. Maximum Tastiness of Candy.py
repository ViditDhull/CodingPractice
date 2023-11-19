class Solution(object):
    def maximumTastiness(self, price, k):
        if k == 0:
            return 0
        price.sort()
        def isValid(num):
            n = len(price)
            cnt = 1
            diff = price[0] + num
            for i in range(1,n):
                if price[i] >= diff:
                    diff = price[i] + num
                    cnt += 1
                else:
                    continue
            return cnt
        low,high = 0,max(price) - min(price)
        ans = -1
        while low <= high:
            mid = (low + high) >> 1
            if isValid(mid) >= k:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans