class cycleChecker:
    def __init__(self,G):
        super().__init__()
        self.visited = [False]*len(G)
        self.prev = [None]*len(G)
        self.graph = G
        self.recstack = [False]*len(G)

    def cycleCheck(self):
        x = self.dfs(0)
        return x

    def cycleCheck(self):
        for node in 
    def dfs(self,svtx):
        self.visited[svtx] = True
        for neighbour in self.graph[svtx]:
            if self.visited[neighbour] == False:
                self.visited[neighbour] = True
                self.prev[neighbour] = svtx
                self.dfs(neighbour)
            elif self.prev[svtx] == neighbour:
                return False
        return True


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

    cc = cycleChecker(G)
    print(cc.cycleCheck())


if __name__ == '__main__':
    main()