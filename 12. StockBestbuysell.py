class Stock:
    def max_profit(self, prices):
        l, r = 0, 1
        maxp = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxp = max(maxp, profit)
            else:
                l = r
            r += 1
        return maxp
