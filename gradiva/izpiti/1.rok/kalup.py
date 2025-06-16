class Stack:
    def __init__(self, size=10):
        self.items = [None]*size
        self.top = -1
        self.size = size

    def push(self, item):
        if self.top == self.size-1:
            print('Stack is full!')
            return
        self.top += 1
        self.items[self.top] = item
    
    def pop(self):
        if self.top == -1:
            print('Stack is empty!')
            return None
        item = self.items[self.top]
        self.top -= 1
        return item



def compute(expr):
    stack = Stack(100)
    tokens = expr.split()
    for t in tokens:
        if t == "+":
            a = stack.pop()
            b = stack.pop()
            stack.push(b + a)
        elif t == "*":
            a = stack.pop()
            b = stack.pop()
            stack.push(b * a)
        else:
            stack.push(int(t))
    return stack.pop()