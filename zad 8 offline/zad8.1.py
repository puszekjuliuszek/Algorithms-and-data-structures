from zad8testy import runtests
from math import sqrt,ceil
from queue import deque
from copy import deepcopy


def lenth(x1,y1,x2,y2):
    return ceil(sqrt((x1-x2)**2 + (y1-y2)**2))

def is_spanning(G):
    que = deque()
    que.append(0)
    visited = [False for _ in range(len(G))]
    visited[0] = True
    while que:
        current = que.popleft()
        visited[current] = True
        for i in G[current]:
            if not visited[i]:
                que.append(i)
    for i in visited:
        if not i:
            return False
    return True

def highway( A ):
    edges = []
    n = len(A)
    for i in range(n):
        for j in range(i+1,n):
            edges.append([lenth(A[i][0],A[i][1],A[j][0],A[j][1]),i,j])
    edges.sort()
    vertex = [[j for j in range(n) if j!=i] for i in range(n)]

    edges_cpy = edges.copy()
    vertex_cpy = deepcopy(vertex)

    minn = float('inf')
    while(is_spanning(vertex_cpy)):
        lenn,v1,v2 = edges_cpy.pop(0)
        for i in range(len(vertex_cpy[v1])):
            if vertex_cpy[v1][i] == v2:
                vertex_cpy[v1].pop(i)
                break
        for i in range(len(vertex_cpy[v2])):
            if vertex_cpy[v2][i] == v1:
                vertex_cpy[v2].pop(i)
                break

        edges_cpy2 = edges_cpy.copy()
        vertex_cpy2 = deepcopy(vertex_cpy)

        while(is_spanning(vertex_cpy2)):
            minn = min(minn, (edges_cpy2[-1][0] - edges_cpy2[0][0]))
            lenn, v1,v2 = edges_cpy2.pop()
            for i in range(len(vertex_cpy2[v1])):
                if vertex_cpy2[v1][i] == v2:
                    vertex_cpy2[v1].pop(i)
                    break
            for i in range(len(vertex_cpy2[v2])):
                if vertex_cpy2[v2][i] == v1:
                    vertex_cpy2[v2].pop(i)
                    break



    return minn

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )