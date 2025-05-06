import networkx as nx
import matplotlib.pyplot as plt


class GraphAL:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def is_edge(self, u, v):
        return v in self.adj_list[u]

    def get_neighbors(self, u):
        return self.adj_list[u]

    def bfs(self, start):
        visited = [False] * self.n
        queue = [start]
        visited[start] = True
        while queue:
            u = queue.pop(0)
            print(u, end=' ')
            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
    
    
    # prikaže ta graf - potrebni sta matplotlib in networkx
    def show(self):
        G = nx.Graph()
        for u in range(self.n):
            for v in self.adj_list[u]:
                G.add_edge(u, v)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()


 

