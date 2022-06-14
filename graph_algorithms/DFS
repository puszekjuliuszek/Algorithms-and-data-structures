# typical dfs form Cormen, but dfs_visit is iterative not recursion
# implementation for graph as a matrix wich returs list of parents, because idk what else it sould retun


def Dfs(G: list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]

    for i in range(n):
        if not visited[i]:
            Dfs_visit(G, i, visited, parents)

    return parents


def Dfs_visit(G: list, s: int, visited: list, parents: list) -> None:
    n = len(G)
    stack = [s]
    visited[s] = True
    while len(stack) > 0:
        u = stack.pop()
        visited[u] = True
        for i in range(n):
            if not visited[i] and G[u][i] != float('inf'):
                parents[i] = u
                stack.append(i)


if __name__ == "__main__":
    inf = float('inf')
    G = [[inf, 2, inf, 3, inf, inf, inf, inf, 1],
         [2, inf, 5, inf, inf, inf, inf, inf, inf],
         [inf, 5, inf, inf, inf, 1, inf, inf, inf],
         [3, inf, inf, inf, 3, inf, 1, inf, inf],
         [inf, inf, inf, 3, inf, 8, inf, 1, inf],
         [inf, inf, 1, inf, 8, inf, inf, 4, inf],
         [inf, inf, inf, 1, inf, inf, inf, 7, 2],
         [inf, inf, inf, inf, 1, 4, 7, inf, inf],
         [1, inf, inf, inf, inf, inf, 2, inf, inf]]

    print(Dfs(G))
