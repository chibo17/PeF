import matplotlib.pyplot as plt
import networkx as nx

class NaiveDisjointSets:
    def __init__(self, n):
        self.name = list(range(n))

    def union(self, u, v):
        name_u = self.name[u]
        name_v = self.name[v]
        for i in range(len(self.name)):
            if self.name[i] == name_v:
                self.name[i] = name_u


class DisjointSets:
    def __init__(self, n):
        self.name = list(range(n))
    
    def find(self, i):
        while self.name[i] != i:
            i = self.name[i]
        return i
    
    def union(self, u, v):
        name_u = self.find(u)
        name_v = self.find(v)
        self.name[name_v] = name_u


class GraphWAL:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

    def is_edge(self, u, v):
        return any(v == neighbor[0] for neighbor in self.adj_list[u])

    def get_neighbors(self, u):
        return [neighbor[0] for neighbor in self.adj_list[u]]
    
    # uporaba naivnih disjunktnih množic
    def kruskal_simple(self):
        ds = NaiveDisjointSets(self.n)
        edges = []
        for u in range(self.n):
            for v, w in self.adj_list[u]:
                if u < v:
                    edges.append((w, u, v))
        edges.sort()
        mst = GraphWAL(self.n)
        for w, u, v in edges:
            if ds.name[u] != ds.name[v]:
                ds.union(u, v)
                mst.add_edge(u, v, w)
        return mst
    
    
    def show(self):
        G = nx.Graph()
        for u in range(self.n):
            for v, w in self.adj_list[u]:
                G.add_edge(u, v, weight=w)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()
        