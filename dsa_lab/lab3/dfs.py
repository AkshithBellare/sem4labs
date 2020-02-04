	

class DFS:
    def __init__(self,G):
        self.visited = [False]*len(G)
        self.start = [0]*len(G)
        self.fin = [0]*len(G)
        self.prev = [None]*len(G)
        self.time = 0
        self.G = G
        self.tree_edges = []
        self.back_edges = []

    def dfs(self,u):
        self.visited[u] = True
        self.start[u] = self.time
        self.time = self.time+1
        for v in self.G[u]:
            if self.visited[v] is False:
                self.prev[v] = u
                self.tree_edges.append((u,v))
                self.dfs(v)
            elif self.prev[u] != v:
                self.back_edges.append((u,v))
        self.fin[u] = self.time
        self.time = self.time+1
        
    def print_time(self):
        for i in range(len(self.G)):
            print(f"{i} : start - {self.start[i]}, end - {self.fin[i]}")
        print("Tree edges are : ")
        print(self.tree_edges)
        print("Back edges are : ")
        print(self.back_edges)
    

def main():
    ''' Adjacency List representation. G is a list of lists. '''
    G = [] 

    file=open('input.txt','r')
    for line in file:
        line=line.strip()
        adjacentVertices = []
        first=True
        for node in line.split(' '):
            if first:
                first=False
                continue
            adjacentVertices.append(int(node))
        G.append(adjacentVertices)

    file.close()

    d = DFS(G)
    print(G)
    d.dfs(0)
    d.print_time()

if __name__ == '__main__':
    main()

