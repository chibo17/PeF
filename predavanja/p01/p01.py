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

def test(d, f):
    start = time.time()
    for i in range(100000):
        x = random.choice(d)
        f(x,d)
    end = time.time()
    return end-start

inputs = range(1000, 10000, 1000)

times_n = []
times_log = []
for n in inputs:
    t1 = test(list(range(n)), find)
    t2 = test(list(range(n)), bisection_find)
    times_n.append(t1)
    times_log.append(t2)

plt.plot(inputs, times_n)
plt.plot(inputs, times_log)
plt.show()
