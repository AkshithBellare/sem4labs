from collections import deque

def bfs(G,svtx):
    s = int(svtx)
    num_of_vtx = len(G)
    color = [0] * num_of_vtx
    distance = [9999] * num_of_vtx
    predecessor = [-1] * num_of_vtx
    color[s] = 1
    distance[s] = 0
    predecessor[s] = -1
    queue = deque()
    queue.append(s)
    while len(queue)!=0:
        vtx = queue.popleft()
        for neighbour in G[vtx]:
            if color[neighbour] == 0:
                color[neighbour] = 1
                distance[neighbour] = distance[vtx] + 1
                print("vtx:",neighbour,"visited distance:",distance[neighbour])
                predecessor[neighbour] = vtx
                queue.append(neighbour)
        color[vtx] = 2
    
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
    vtx = input('Enter source vertex for bfs:')
    bfs(G,vtx)

if __name__ == '__main__':
    main()


