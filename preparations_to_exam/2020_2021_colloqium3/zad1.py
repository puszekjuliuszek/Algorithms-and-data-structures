from zad1testy import runtests
from collections import deque

def Floyd_Warshall(M):
    n = len(M)
    D = [[M[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j]> D[i][k]+D[k][j]:
                    D[i][j] = D[i][k]+D[k][j]

    return D


def bfs(M,s,t):
    n = len(M)

    visited = [False for _ in range (n)]
    parents = [None for _ in range (n)]
    que = deque()
    que.append((s,None))
    while que:
        u,parent = que.popleft()
        visited[u] = True
        parents[u] = parent
        if u == t:
            return parents
        for v in range(n):
            if not visited[v] and M[u][v] != float('inf'):
                que.append((v,u))


def make_path(parents,end):
    path = []
    path.append(end)
    curr = end
    while parents[curr] != None:
        path.append(parents[curr])
        curr = parents[curr]
    return path

def keep_distance(M, x, y, d):
    n = len(M)
    for row in M:
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = float('inf')

    distances = Floyd_Warshall(M)

    vertex = []
    for i in range(n):
        for j in range(n):
            if distances[i][j]>=d:
                vertex.append((i,j))

    graph = [[float('inf') for _ in range(len(vertex))] for _ in range(len(vertex))]
    for i in range(len(vertex)):
        for j in range(len(vertex)):
            c1,m1 = vertex[i]
            c2,m2 = vertex[j]
            if c1!=m2 and c2!=m1 and M[m1][m2]<float('inf') and M[c1][c2]<float('inf'):
                graph[i][j] = 1

    start,end = 0,0
    for i in range(len(vertex)):
        c,m = vertex[i]
        if c == x and m == y:
            start= i
        elif c == y and m== x:
            end = i

    parents = bfs(graph,start,end)
    path = make_path(parents,end)

    real_path = []
    for v in range(len(path) -1, -1,-1):
        real_path.append(vertex[path[v]])







    return real_path


runtests( keep_distance )
