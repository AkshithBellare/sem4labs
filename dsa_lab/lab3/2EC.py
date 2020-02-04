class DFS2e:
    def __init__(self,G):
        super().__init__()
        num_of_vtx = len(G)
        self.G = G
        self.visited = [False]*num_of_vtx
        self.start = [0]*num_of_vtx
        self.finish = [0]*num_of_vtx
        self.prev = [-1]*num_of_vtx
        self.time = 0
        self.sst = 0
        
    
    def is2EC(self):
        self.dfs_2e(0)

    def dfs_2e(self,u):
            u = int(u)
            self.visited[u] = True
            self.start[u] = self.time
            self.sst = self.start[u]
            self.time += 1
            for neighbour in self.G[u]: 
                if self.visited[int(neighbour)] == False:
                    self.prev[int(neighbour)] = u
                    self.sst = min(self.dfs_2e(neighbour),self.sst)
                elif self.visited[int(neighbour)] == True and self.prev[u]!=neighbour:
                    self.sst = min(self.sst,self.start[int(neighbour)])
            self.finish[u] = self.time
            self.time +=1
            if self.sst < self.start[u]:
                return self.sst
            elif self.sst == self.start[u] and self.start[u]!=0:
                print("Graph is not two edge connected")
                exit(0)

        
def main():
    file = open("input.txt","r")
    G = []
    for line in file:
        line = line.strip()
        first = True
        adjacentVertices = []
        for node in line.split(' '):
            if first is True:
                first = False
                continue
            adjacentVertices.append(node)
        G.append(adjacentVertices)
    print(G)

    D = DFS2e(G)
    D.is2EC()
if __name__ == "__main__":
    main()