class AdjacencyList:
    def __init__(self,numvertex):
        self.numvertex = numvertex
        self.verticesList = [[]*numvertex for i in range(numvertex)]

    def set_edge(self,frm,to):
        #check if vertex in list add only if its not in list
        if to not in self.verticesList[frm]:
            self.verticesList[frm].append(to)

    def graph_print(self):
        for i in range(self.numvertex):
            print(self.verticesList[i])

G = AdjacencyList(6)
G.set_edge(0,1)
G.set_edge(3,2)
G.set_edge(3,4)
G.graph_print()