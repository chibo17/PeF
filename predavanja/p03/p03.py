import random
import time
import matplotlib.pyplot as plt

def merge(a,b):
	c = []
	i = j = 0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			c.append(a[i])
			i+=1
		else:
			c.append(b[j])
			j+=1
	c.extend(a[i:])
	c.extend(b[j:])
	return c

def merge_sort(a):
	n = len(a)
	if n <= 1:
		return a
	else:
		mid = n//2
		left = merge_sort(a[:mid])
		right = merge_sort(a[mid:])
		return merge(left,right)


def lomuto_partition(a,low,high):
	pivot = a[high]
	i = low
	for j in range(low,high):
		if a[j] <= pivot:
			a[i],a[j] = a[j],a[i]
			i+=1
	a[i],a[high] = a[high],a[i]
	return i

def quick_sort(a):
	n = len(a)
	if n <= 1:
		return a
	else:
		pivot = a[0]
		less = [x for x in a if x < pivot]
		eq = [x for x in a if x == pivot]
		greater = [x for x in a if x > pivot]
		return quick_sort(less) + eq +quick_sort(greater)

def make_random_list(n):
	return [random.randint(1,100000) for i in range(n)]


def test_sort(sort_function, l):
	a = l
	start = time.time()
	sort_function(a)
	end = time.time()
	return end-start

measure_merge = []
measure_quick = []
for n in range(1000,100000,10000):
	l = make_random_list(n)
	t1 = test_sort(merge_sort,l)
	t2 = test_sort(quick_sort,l)
	measure_merge.append(t1)
	measure_quick.append(t2)

plt.plot(range(1000,100000,10000),measure_merge,label='Merge sort')
plt.plot(range(1000,100000,10000),measure_quick,label='Quick sort')
plt.legend()
plt.show()