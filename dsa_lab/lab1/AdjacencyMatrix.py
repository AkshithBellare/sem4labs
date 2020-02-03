class Graph:
    def __init__(self, numvertex):
        self.adjMatrix = [[0]*numvertex for x in range(numvertex)]
        self.numvertex = numvertex
        self.verticeslist = [0] * numvertex
    
    def set_vertex(self,vtx):
        if 0<=vtx<=self.numvertex:
            self.verticeslist[vtx] = 1

    def set_edge(self,frm,to):
        self.adjMatrix[frm][to] = 1
    
    def print_matrix(self):
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                print(self.adjMatrix[i][j],end='  ')
            print("\n")

G = Graph(6)
G.set_vertex(0)
G.set_vertex(1)
G.set_vertex(2)
G.set_vertex(3)
G.set_vertex(4)
G.set_vertex(5)
G.set_edge(0,5)
G.set_edge(1,2)
G.set_edge(0,3)
G.set_edge(4,2)
G.print_matrix()


