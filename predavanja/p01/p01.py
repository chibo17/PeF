import time
import random
import matplotlib.pyplot as plt

def find(x, d):
    for i in d:
        if x == i:
            return True
    return False

def binary_search(x, d):
    left = 0
    right = len(d) - 1
    while left <= right:
        mid = (left + right) // 2
        if x == d[mid]:
            return True
        elif x < d[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return False

measurements = []
measurements_binary = []
for i in range(10000, 100000, 10000):
    d = list(range(i))
    time_avg = 0
    time_avg_binary = 0
    for j in range(1000):       
        start = time.time()
        x = random.randint(0, i)
        find(x, d)
        end = time.time()
        start_binary = time.time()
        binary_search(x, d)
        end_binary = time.time()  
        time_avg_binary += end_binary - start_binary  
        time_avg += end - start
    measurements.append( time_avg / 1000 )
    measurements_binary.append( time_avg_binary / 1000 )

plt.plot(range(10000, 100000, 10000), measurements)
plt.plot(range(10000, 100000, 10000), measurements_binary)
plt.show()
