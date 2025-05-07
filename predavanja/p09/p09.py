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
        paths = [None] * self.n
        paths[start] = -1
        while queue:
            u = queue.pop(0)
            print(u, end=' ')
            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    paths[v] = u
                    queue.append(v)
        return paths
    
    
    # prikaže ta graf - potrebni sta matplotlib in networkx
    def show(self):
        G = nx.Graph()
        for u in range(self.n):
            for v in self.adj_list[u]:
                G.add_edge(u, v)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        plt.show()

# iz tabele (paths) dobimo pot
def get_path(paths, end):
    path = []
    while end != -1:
        path.append(end)
        end = paths[end]
    return path

 


# Uteženi graf - povezave so utežene
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

    def dijkstra(self, start):
        visited = [False] * self.n
        dist = [float('inf')] * self.n
        dist[start] = 0
        queue = [start]
        paths = [None] * self.n
        paths[start] = -1
        while queue:
            u = min(queue, key=lambda x: dist[x])
            print(u, self.adj_list[u])
            queue.remove(u)
            visited[u] = True
            for v, w in self.adj_list[u]:
                if not visited[v]:
                    if dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        paths[v] = u
                        if v not in queue:
                            queue.append(v)
        return dist, paths
    
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


# Labirinti
def maze_to_graph(maze):
    n= len(maze)
    m= len(maze[0])
    g= GraphAL(n*m)
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                start = i*m+j
            if maze[i][j] == 'E':
                end = i*m+j
                
            if maze[i][j] == ' ' or maze[i][j] == 'S' or maze[i][j] == 'E':
                if i > 0 and maze[i-1][j] == ' ':
                    g.add_edge(i*m+j, (i-1)*m+j)
                if i < n-1 and maze[i+1][j] == ' ':
                    g.add_edge(i*m+j, (i+1)*m+j)
                if j > 0 and maze[i][j-1] == ' ':
                    g.add_edge(i*m+j, i*m+(j-1))
                if j < m-1 and maze[i][j+1] == ' ':
                    g.add_edge(i*m+j, i*m+(j+1))
    return g, start, end

def read_maze_from_file(filename):
    with open(filename, 'r') as f:
        maze = [line.strip() for line in f.readlines()]
    return maze