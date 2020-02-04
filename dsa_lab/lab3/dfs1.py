class DFS():
    def __init__(self,G):
        super().__init__()
        self.graph = G
        self.num_of_vtx = len(G)
        self.visited = [False]*self.num_of_vtx
        self.time = 0
        self.start = [0]*self.num_of_vtx
        self.finish = [0]*self.num_of_vtx
        self.tree_edges = []
        self.back_edges = []
        self.prev = [-1]*self.num_of_vtx

        
    def dfs(self,svtx):
        svtx = int(svtx)
        self.visited[svtx] = True
        self.start[svtx] = self.time
        self.time += 1
        for neighbour in self.graph[svtx]:
            neighbour = int(neighbour)
            if self.visited[neighbour] is False:
                self.prev[neighbour] = svtx
                print('visited vertex:',neighbour)
                self.tree_edges.append((svtx,neighbour))
                self.dfs(neighbour)
            elif self.prev[svtx]!=neighbour and self.prev[neighbour]!= -1:
                    self.back_edges.append((neighbour,svtx))
        self.finish[svtx] = self.time
        self.time += 1

    def printTime(self):
        for i in range(self.num_of_vtx):
            print(i,': start-> ',self.start[i],' end-> ',self.finish[i])

    def printEdges(self):
        print('Tree edges-> ',self.tree_edges)
        print('Back edges-> ',self.back_edges)

def main():
    file = open("input.txt","r")
    G = []
    for line in file:
        line = line.strip()
        adjacentVertices = []
        first = True
        for node in line.split(' '):
            if first==True:
                first = False
                continue
            adjacentVertices.append(node)
        G.append(adjacentVertices)
    print(G)
    D = DFS(G)
    D.dfs(0)
    D.printTime()
    D.printEdges()

if __name__ == "__main__":
    main()