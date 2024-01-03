class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l_prices = len(prices)
        if l_prices < 2:
            return 0
        lp = 0
        rp = 1
        mp = 0
        while rp < l_prices:
            if prices[lp] < prices[rp]:
                if mp < abs(prices[lp] - prices[rp]):
                    mp = abs(prices[rp] - prices[lp])
                rp += 1
            else:
                lp = rp
                rp += 1
        return mp