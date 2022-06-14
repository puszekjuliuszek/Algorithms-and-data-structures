#relaxation is hidden in the djikstra function

def min_id(T: list, used: list) -> int:
    m = float('inf')
    id = None
    for i in range(0, len(T)):
        if not used[i] and T[i] < m:
            m = T[i]
            id = i
    return id


def Djikstra(G: list, s: int) -> tuple:
    n = len(G)
    T = [float('inf') for i in range(n)]
    T[s] = 0
    used = [False for i in range(n)]
    parents = [None for i in range(n)]
    count = 0

    while count < n:
        u = min_id(T, used)
        if u is None:
            break

        for v in range(n):
            if not used[v]:
                # relaxation
                if T[u] + G[u][v] < T[v]:
                    T[v] = T[u] + G[u][v]
                    parents[u] = v

        used[u] = True
        count += 1

    return T, parents


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
    
    print(Djikstra(G,0))
