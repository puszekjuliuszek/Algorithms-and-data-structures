class Node:
    def __init__(self,value):
        self.parent = self
        self.value = value
        self.rank = 0

def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent

def union(x,y):
    x=find(x)
    y = find(y)
    if x==y:
        return
    if x.rank>y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

def Kursal(G):
    n = len(G)
    vertex = [Node(i) for i in range(n)]

    edges = []
    for i in range(n):
        for j in range(i,n):
            if G[i][j]<float('inf'):
                edges.append((i,j,G[i][j]))
    edges.sort(key=lambda x:x[2])

    how_many_edges = 0
    i = 0
    mst = []

    while how_many_edges <n-1:
        u,v,length = edges[i]
        i+=1

        if find(vertex[u]) != find(vertex[v]):
            union(vertex[u],vertex[v])
            mst.append((u,v,length))
            how_many_edges+=1

    return mst

if __name__ == "__main__":
    inf = float('inf')
    G = [[inf,2,inf,3,inf,inf,inf,inf,1],
         [2,inf,5,inf,inf,inf,inf,inf,inf],
         [inf,5,inf,inf,inf,1,inf,inf,inf],
         [3,inf,inf,inf,3,inf,1,inf,inf],
         [inf,inf,inf,3,inf,8,inf,1,inf],
         [inf,inf,1,inf,8,inf,inf,4,inf],
         [inf,inf,inf,1,inf,inf,inf,7,2],
         [inf,inf,inf,inf,1,4,7,inf,inf],
         [1,inf,inf,inf,inf,inf,2,inf,inf]]

    print(Kursal(G))

