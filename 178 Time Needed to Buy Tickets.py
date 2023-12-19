class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        return sum(min(v, tickets[k] if i <= k else tickets[k] - 1) for i, v in enumerate(tickets))