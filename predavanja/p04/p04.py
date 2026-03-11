
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



# kalkulator 

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
            

class Queue:
    def __init__(self, size=10):
        self.items = [None]*size
        self.front = 0
        self.num_el = 0
        self.size = size

    def enqueue(self, item):
        if self.num_el == self.size:
            print('Queue is full!')
            return
        self.items[(self.front + self.num_el) % self.size] = item
        self.num_el += 1

    def dequeue(self):
        if self.num_el == 0:
            print('Queue is empty!')
            return None
        item = self.items[self.front]
        self.front = (self.front + 1) % self.size
        self.num_el -= 1
        return item



# iskanje z bisekcijo
def binary_search(items, item):
    left = 0
    right = len(items) - 1
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == item:
            return mid
        elif items[mid] < item:
            left = mid + 1
        else:
            right = mid - 1
    return -1

class SetA:
    def __init__(self, universal_set):
        self.universal_set = sorted(universal_set) # uredimo zaradi hitrejšega iskanja
        self.items = [False]*len(universal_set)
        self.size = len(universal_set)
  
    
    def add(self, item):
        index = binary_search(self.universal_set, item)
        if index != -1 :
            self.items[index] = True
     
    
    def remove(self, item):
        index = binary_search(self.universal_set, item)
        if index != -1 :
            self.items[index] = False
    
    
    def contains(self, item):
        index = binary_search(self.universal_set, item)
        if index != -1 :
            return self.items[index]
        return False
    
    def print(self):
        print('{ ', end='')
        for i in range(self.size):
            if self.items[i]:
                print(self.universal_set[i], end=' ')
        print('}')
        
class LinkedList:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def add(self, item):
        l = LinkedList(item)
        l.next = self
        return l

    def delete(self, x):
        current = self
        prev = None
        while current:
            if current.item == x:
                if prev:
                    prev.next = current.next
                    return self
                else:
                    return current.next
            prev, current = current, current.next
        return self 

    # TODO: remove first

    # TODO: append

    # TODO: remove item

    # TODO: reverse

    # TODO: concatenate


    def print(self):
        l = self
        while l is not None:
            print(l.item, end=' ')
            l = l.next
        print()
