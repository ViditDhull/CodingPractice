from collections import deque
class MyStack(object):

    def __init__(self):
        self. container = deque()

    def push(self, x):
        return self.container.append(x)
        

    def pop(self):
        return self.container.pop()
        

    def top(self):
        return self.container[-1]
        

    def empty(self):
        return len(self.container) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()