from zad8testy import runtests
import math
def highway( A ):
    class Node:
        def __init__(self):
            self.parent = self
            self.rank = 0
    def find(x):
        if x.parent!=x:
            x.parent=find(x.parent)
        return x.parent
    def union(x,y):
        x = find(x)
        y = find(y)
        if x==y:
            return
        if (x.rank>y.rank):
            y.parent = x
        else:
            x.parent = y
            if(x.rank==y.rank):
                y.rank+=1
    n = len(A)
    edges_in_tree=n-1
    Vertex = [Node() for _ in range(n)]
    edges = []
    for i in range(0,n):
        for j in range(i+1,n):
            edges.append([Vertex[i],Vertex[j],math.ceil(math.sqrt((A[j][0]-A[i][0])**2+(A[j][1]-A[i][1])**2))])
    edges.sort(key= lambda x:x[2])
    roznica = math.inf
    edges_amount=len(edges)
    for i in range(0,edges_amount):
        counter=0
        Edgemin=edges[i][2]
        Edgemax=0
        for j in range(i,edges_amount):
            if(find(edges[j][0])!=find(edges[j][1])):
                counter+=1
                union(find(edges[j][0]),find(edges[j][1]))
                Edgemax=edges[j][2]
                if(roznica<Edgemax-Edgemin or counter>=edges_in_tree):
                    break
        if(counter == edges_in_tree and roznica>Edgemax-Edgemin):
            roznica=Edgemax-Edgemin
        for j in range(n):
            Vertex[j].rank=0
            Vertex[j].parent=Vertex[j]
    return roznica

# zmien all_tests na True zeby uruchomic wszystkie testy
#print(highway([(100, 100), (100, 200), (200, 100), (200, 200)]))
runtests( highway, all_tests = True )