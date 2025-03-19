


def rangeN(n):
    if n == 1:
        l = LinkedList(0)
        return l
    l = rangeN(n-1)
    h = LinkedList(0)
    l.plus1()
    h.next = l
    return h

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
    
    def plus1(self):
        self.item += 1
        if self.next == None:
            return
        self.next.plus1()
        return

    def sum(self):
        if self.next == None:
            return self.item
        return self.item+self.next.sum()
    
    def maks(self):
        if self.next == None:
            return self.item
        return max(self.item, self.next.maks())
    
    def reduce(self, f):
        if self.next == None:
            return self.item
        return f(self.item, self.next.reduce(f))

    def concat(self, l):
        if self.next == None:
            self.next = l
            return
        self.next.concat(l)
    
    def zip(self, l):
        if self.next == None and l.next == None:
            z = LinkedList((self.item, l.item))
            return z
        restZ = self.next.zip(l.next)
        z = LinkedList((self.item, l.item))
        z.next = restZ
        return z

    def print(self):
        l = self
        while l is not None:
            print(l.item, end=' ')
            l = l.next
        print()



# -------- Razpršena tabela -----------
def string2num(s):
    num = 0
    for c in s:
        num*=256
        num+=ord(c)
    return num




# metoda deljenja
def hash_division(key, table_size):
    return key % table_size

# metoda množenja
def hash_multiplication(key, table_size, A=(5**0.5 - 1) / 2):
    return int(table_size * (key * A % 1))



class HashTableOpen:
    def __init__(self, table_size, hash_function):
        self.table_size = table_size
        self.hash_function = hash_function
        self.table = [None] * table_size
  
    def insert(self, key, value):
        index = self.hash_function(key, self.table_size)
        while self.table[index] is not None:
            index = (index + 1) % self.table_size
        self.table[index] = key, value 

    
    def get(self, key):
        index = self.hash_function(key, self.table_size)   
        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                return v
            index = (index + 1) % self.table_size
        return None


class HashTableChaining:
    def __init__(self, table_size, hash_function):
        self.table_size = table_size
        self.hash_function = hash_function
        self.table = [[] for _ in range(table_size)]

    def insert(self, key, value):
        index = self.hash_function(key, self.table_size)
        self.table[index].append((key, value))
  
    def get(self, key):
        index = self.hash_function(key, self.table_size)
        for i in range(len(self.table[index])):
            k,v = self.table[index][i]
            if  k == key:
                return v
        return None  