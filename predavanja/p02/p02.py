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