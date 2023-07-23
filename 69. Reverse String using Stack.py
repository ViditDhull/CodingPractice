from collections import deque

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
    
    def reverse_string(self, string_ele):
        for i in string_ele:
            self.container.append(i)
        reverse_stk = []
        for i in range(len(self.container)):
            reverse_stk.append(self.pop())
        return ''.join(reverse_stk)

s = Stack()
print(s.reverse_string("We will conquere COVID-19"))



# def reverse_string(s):
#     stack = Stack()

#     for ch in s:
#         stack.push(ch)

#     rstr = ''
#     while stack.size()!=0:
#         rstr += stack.pop()

#     return rstr