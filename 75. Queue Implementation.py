# # Using Lists
# stock_price = []

# stock_price.insert(0, 131.10)
# stock_price.insert(0, 132.10)
# stock_price.insert(0, 133.10)

# print(stock_price) # >> [133.10, 132.10, 131.1]
# #The first one to go in pops out first. Because the elements keeps shifting one position to left (increasing index)
# stock_price.pop() # >> 131.10
# stock_price.pop() # >> 132.10
# stock_price.pop() # >> 133.10

# Using deque()

from collections import deque

q = deque()

q.appendleft(5)
q.appendleft(8)
q.appendleft(27)

q.pop() # >> 5
q.pop() # >> 8
q.pop() # >> 27

# Our own class for Queue

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    

pq = Queue()

pq.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.01 AM',
    'price' : 131.10
})

pq.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.02 AM',
    'price' : 132.10
})

pq.enqueue({
    'company' : 'Wal Mart',
    'timestamp' : '15 apr, 11.03 AM',
    'price' : 135.10
})

print(pq.buffer)

print(pq.dequeue())