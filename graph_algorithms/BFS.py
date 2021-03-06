from queue import deque


def bfs(G, s):
    que = deque()
    que.append(s)

    # paths structure:
    #   element no. i is a list:
    #       i is the number of vertex we are talking about
    #       0-index: number of tilde (how many edges we have to pass from beggining of the graph)
    #       1-index: list of parents (maybe we can get to our vertex no. i from several previous vertexes 
    #               on the same tilde)

    paths = [None for _ in range(len(G))]
    paths[s] = [0, []]
    
    while que:
        current = que.popleft()
        for i in G[current]:
            if paths[i] == None:
                paths[i] = [paths[current][0] + 1, [current]]
                que.append(i)
            elif paths[i][0] == paths[current][0] + 1 and current not in paths[i][1]:
                paths[i][1].append(current)
                
    return paths


if __name__ == "__main__":
    G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12],
         [10, 11]]

    print(bfs(G, 0))
