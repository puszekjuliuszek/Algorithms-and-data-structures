
def Dfs(G: list) -> list:
    n = len(G)
    time = 0
    times = [float('inf') for _ in range(n)]
    parents = [None for _ in range(n)]
    sorted_vertex = []
    for i in range(n):
        if  times[i] == float('inf'):
            Dfs_visit(G, i, time, times, parents,sorted_vertex)

    return sorted_vertex


def Dfs_visit(G: list, s: int, time: int, times: list, parents: list,sorted_vertex: list) -> None:
    n = len(G)
    time += 1
    times [s] = time
    for i in range(n):
        if times[i] == float('inf') and G[s][i] != float('inf'):
            parents[i] = s
            Dfs_visit(G,i,time,times,parents,sorted_vertex)
    sorted_vertex.append(s)




    return sorted_vertex.reverse()

if __name__ == "__main__":
    inf = float('inf')
    G = [[inf, inf, inf,inf, 1, 1, inf, inf, inf,inf, inf, 1, inf, inf],
         [inf, inf, 1,inf, 1, inf, inf, inf, 1,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, 1, 1, inf, inf,inf, 1, inf, inf, inf],
         [inf, inf, 1,inf, inf, inf, 1, inf, inf,inf, inf, inf, inf, 1],
         [inf, inf, inf,inf, inf, inf, inf, 1, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, 1,inf, inf, inf, 1, inf],
         [inf, inf, inf,inf, inf, 1, inf, inf, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, 1, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, 1],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,1, inf, 1, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, 1, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf]]

    
    print(Dfs(G))
