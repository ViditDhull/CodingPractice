class RecentCounter(object):

    def __init__(self):
        self.requests = []

    def ping(self, t):
        up_range = 0
        low_range = -3000
        self.requests.append(t)
        up_range += t
        low_range += t
        counter = 0
        for i in self.requests:
            if i >= low_range and i <= up_range:
                counter += 1
        return counter



# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)