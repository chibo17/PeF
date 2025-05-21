import matplotlib.pyplot as plt
import numpy as np
import time
import networkx as nx

# ------------------- kompleksnost --------------------

def linear(n):
    a=0
    for i in range(n):
        a = a+1
# nlogn
def lingarithmic(n):
    for i in range(n):
        a=1
        while a<n:
            a = a*2
        
def quadratic(n):
    a=0
    for i in range(n):
        for j in range(n):
            a+=1

def power2(n):
    if n==1:
        return
    else:
        power2(n-1)
        power2(n-1)
        return

def faktoriela(n):
    if n==1:
        return
    else:
        for i in range(n):
            faktoriela(n-1)
        return

# meritve
def measure_time(func, n):
    start_time = time.time()
    func(n)
    end_time = time.time()
    return end_time - start_time

def plot_time_complexity(func, n_values):
    times = [measure_time(func, n) for n in n_values]
    plt.plot(n_values, times, label=f'Time complexity of {func.__name__}')
    plt.xlabel('Input size (n)')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity')
    plt.legend()
    plt.show()


# ------------------- terke --------------------


def gen3tuple(k):
    tuples = []
    for i in range(k):
        for j in range(k):
            for l in range(k):
                tuples.append((i,j,l))
    return tuples

def genNtuple(n,k):
    if n==0:
        return [[]]
    else:
        tuples = []
        smaller_tuples = genNtuple(n-1,k)
        for t in smaller_tuples:
            for i in range(k):
                tuples.append([i]+t)
        return tuples








# ------------------- barvanje --------------------

def read_graph(filename):
    G = nx.DiGraph()  

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()  
            if "->" in line:
                s, d = line.split("->")
                s = s.strip()
                d = d.strip()
                G.add_edge(s, d)  

    return G

def no_hate(graph, coloring):
    count_hate = 0
    for (v1,v2) in graph.edges():
        if coloring[v1] == coloring[v2]:
            count_hate+=1
    return count_hate


def find_colorings(graph, k):
    min_hate = 1000
    min_coloring = None
    for col in genNtuple(len(graph.nodes()), k):
        coloring = {}
        for i, node in enumerate(graph.nodes()):
            coloring[node] = col[i]
        current_hate = no_hate(graph, coloring)
        if current_hate<min_hate:
            min_hate = current_hate
            min_coloring = coloring
            
    return min_hate, min_coloring




# ------------------- podmnožice --------------------





# ------------------- nahrbtnik --------------------




# ------------------- permutacije --------------------



# ------------------- kraljice --------------------