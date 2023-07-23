from collections import deque

stack = deque()

print(dir(stack))

stack.append("Link 1")
stack.append("Link 2")
stack.append("Link 3")
stack.append("Link 4")

stack.pop()     #Returns and removes the last elenent



class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()
    
    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
s = Stack()
s.push(5)

print(s.peek())     #Only returns the element

print(s.pop())      #Returns and removes the element

print(s.is_empty())

s.push(67)
s.push(7)
s.push(3457)

print(s.size())