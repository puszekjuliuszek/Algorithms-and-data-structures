from zad8testy import runtests
from math import sqrt, ceil


class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def lenth(x1, y1, x2, y2):
    return ceil(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))


def is_spanning(G):
    pass


def highway(A):
    n = len(A)
    edges = []
    vertex = [Node(i) for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            edges.append([lenth(A[i][0], A[i][1], A[j][0], A[j][1]), vertex[i], vertex[j]])
    edges = sorted(edges, key=lambda x: x[0])

    minn = float('inf')
    for i in range(n * (n - 1) // 2 - n + 1):
        cnt = 0

        for k in vertex:
            k.parent = k
            k.rank = 0

        for j in range(i, n * (n - 1) // 2):
            if cnt >= n - 1 or minn < edges[j - 1][0] - edges[i][0]:
                break
            lenn, v1, v2 = edges[j]
            if find(v1) != find(v2):
                union(v1, v2)
                cnt += 1
        if cnt >= n - 1:
            minn = min(minn, edges[j - 1][0] - edges[i][0])

    return minn


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(highway, all_tests=True)