class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            index = i + 1
            if i == len(prices) - 1:
                continue
            if prices[i] >= prices[index]:
                prices[i] -= prices[index]
            else:
                while index < len(prices) -1:
                    index += 1
                    if prices[i] >= prices[index]:
                        prices[i] -= prices[index]
                        break

        return prices
