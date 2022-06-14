# typical dfs form Cormen, but dfs_visit is iterative not recursion
# implementation for graph as a matrix wich returs list of parents, because idk what else it sould retun


def Dfs(G: list) -> list:
    n = len(G)
    time = 0
    times = [float('inf') for _ in range(n)]
    parents = [None for _ in range(n)]

    for i in range(n):
        if  times[i] == float('inf'):
            Dfs_visit(G, i, time, times, parents)

    return times


def Dfs_visit(G: list, s: int, time: int, times: list, parents: list) -> None:
    n = len(G)
    stack = [(s,time)]
    times[s] = True
    while len(stack) > 0:
        u,time = stack.pop()
        times[u] = time
        for i in range(n):
            if times[i]>time and G[u][i] != float('inf'):
                parents[i] = u
                stack.append((i,time+1))

def Topological_sort(G):
    n = len(G)
    Times = Dfs(G)
    Times = [(Times[i],i) for i in range (n)]
    Times.sort()
    sorted_vertex = [Times[i][1] for i in range(n)]

    return sorted_vertex

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
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,1, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, 1, inf, inf, inf],
         [inf, inf, inf,inf, inf, inf, inf, inf, inf,inf, inf, inf, inf, inf]]

    print(Topological_sort(G))
