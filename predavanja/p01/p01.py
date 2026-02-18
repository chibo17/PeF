import time
import random
import matplotlib.pyplot as plt


def find(x, d):
    for y in d:
        if x == y:
            return True
    return False

def bisection_find(x,d):
    l = 0
    r = len(d)-1
    while l<=r:
        mid = (l+r)//2
        if x == d[mid]:
            return True
        if x>d[mid]:
            l = mid + 1
        else:
            r = mid -1
    return False

def test(d):
    start = time.time()
    for i in range(100000):
        x = random.choice(d)
        bisection_find(x,d)
    end = time.time()
    return end-start

inputs = range(1000, 1000000, 100000)

for n in inputs:
    print(test(list(range(n))))


