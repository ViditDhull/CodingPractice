import threading
from collections import deque
import time

class Queue:

    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        self.buffer.pop()


order_queue = Queue()

# order_no = 1
def place_order():
    orders = ['pizza','samosa','pasta','biryani','burger']
    
    for i in orders:
        order_queue.enqueue(i)
        print(f'{i} has been added')
        print(order_queue.buffer)
        time.sleep(0.5)

def serve_order():
    while True:
        try:
            order_queue.dequeue()
            print('An order has been served')
            print(order_queue.buffer)
        except:
            print('No orders to serve yet.')
            
        time.sleep(2)



if __name__ == "__main__":
    t1 = threading.Thread(target = place_order)
    t2 = threading.Thread(target = serve_order)

    t1.start()
    t2.start()

    print('Done')