import random
import time
import matplotlib.pyplot as plt

def select_sort(a):
	n = len(a)
	for i in range(n-1):
		m = i
		for j in range(i+1,n):
			if a[j]<a[m]:
				m = j
		a[i], a[m] = a[m],a[i]

def bubble_sort(a):
	n = len(a)
	for i in range(n-1):
		for j in range(n-1):
			if a[j]>a[j+1]:
				a[j], a[j+1] = a[j+1],a[j]
	return a

def insert_sort(arr):
	n = len(arr)
	for i in range(1,n):
		j = i
		while j>0 and arr[j]<arr[j-1]:
			arr[j], arr[j-1] = arr[j-1],arr[j]
			j-=1

def make_random_list(n):
	return [random.randint(1,100000) for i in range(n)]


def test_sort(sort_function, l):
	a = l
	start = time.time()
	sort_function(a)
	end = time.time()
	return end-start

measures_1 = []
measures_2 = []
measures_3 = []
for n in range(1000,10000,1000):
	measures_1.append(test_sort(insert_sort,make_random_list(n)))
	measures_2.append(test_sort(insert_sort,list(range(n))))
	measures_3.append(test_sort(insert_sort,list(range(n,0,-1))))

# insert sort
plt.plot(range(1000,10000,1000), measures_1) #avg case
plt.plot(range(1000,10000,1000), measures_2) #best case
plt.plot(range(1000,10000,1000), measures_3) #worst case
plt.show()