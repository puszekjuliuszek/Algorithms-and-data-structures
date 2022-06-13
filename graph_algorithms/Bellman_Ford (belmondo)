# i like to call this alogorithm Belmondo's algorithm because in polish "Bellmana-Forda sounds a littlile like Belmonda


def min_id(T, used):
    m = float('inf')
    id = None
    for i in range(0, len(T)):
        if not used[i] and T[i] < m:
            m = T[i]
            id = i
    return id


def bellmann_ford(G, s):
    n = len(G)
    T = [float('inf') for i in range(n)]
    T[s] = 0
    used = [False for i in range(n)]
    parents = [None for i in range(n)]
    count = 0
    for u in range(n):
        for v in range(n):
            if not used[v] :
                if T[u] + G[u][v] < T[v]:
                    T[v] = T[u] + G[u][v]
                    parents[u] = v
        used[u] = True
        count += 1
    return T, parents

def bellmann_ford_verify(G,s):
    n = len(G)
    weights, parents = bellmann_ford(G, s)
    for u in range(n):
        for v in range(n):
            if weights[v] > weights[u]  + G[u][v]:
                return False
    return weights,parents

if __name__ == "__main__":
    #lets assume, that we have praph G as a matrix
    #example of usage:

    bellmann_ford_verify(G,0)
