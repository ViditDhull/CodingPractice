class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        result = numBottles
        eb = numBottles
        while eb >= numExchange:
            result += eb // numExchange
            eb = (eb // numExchange) + (eb % numExchange)
        return result