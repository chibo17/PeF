class GraphAM:
    def __init__(self, n):
        self.n = n
        self.matrix = [[False] * n for _ in range(n)]

    def add_edge(self, u, v):
       self.matrix[u][v] = True
       self.matrix[v][u] = True

    def remove_edge(self, u, v):
        self.matrix[u][v] = False
        self.matrix[v][u] = False

    def is_edge(self, u, v):
        return self.matrix[u][v]

    def get_neighbors(self, u):
        neighbors = []
        for v in range(self.n):
            if self.matrix[u][v]:
                neighbors.append(v)
        return neighbors
    
    def degree(self, u):
        return len(self.get_neighbors(u))



class GraphAL:
    def __init__(self, n):
        self.n = n
        self.adj_list = [[] for _ in range(n)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def remove_edge(self, u, v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)

    def is_edge(self, u, v):
        return v in self.adj_list[u]

    def get_neighbors(self, u):
        return self.adj_list[u]

    def dfs_rec(self, u, visited):
        print(u, end=' ')
        visited[u] = True
        for v in self.adj_list[u]:
            if not visited[v]:
                self.dfs_rec(v, visited)

    def dfs_iter(self, u):
        visited = [False] * self.n
        stack = [u]
        while stack:
            v = stack.pop()
            if not visited[v]:
                print(v, end=' ')
                visited[v] = True
                for neighbor in self.adj_list[v]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
    
    def is_connected(self):
        visited = [False] * self.n
        self.dfs_rec(0, visited)
        return all(visited)