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

def is_balanced(str_ele):
    s = Stack()

    result = True
    count1 = 0
    count2 = 0
    count3 = 0
    for ch in str_ele:
        if ch == '(':
            count1 += 1
        elif ch == '{':
            count2 += 1
        elif ch == '[':
            count3 += 1                
        elif ch == ')':
            count1 -= 1
            if count1 < 0:
                result = False
        elif ch == '}':
            count2 -= 1
            if count2 < 0:
                result = False
        elif ch == ']':
            count3 -= 1
            if count3 < 0:
                result = False
    return result

print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
print(is_balanced("((a+g))"))