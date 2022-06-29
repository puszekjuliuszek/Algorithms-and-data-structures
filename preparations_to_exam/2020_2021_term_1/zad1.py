from zad1testy import runtests

def dfs(graph,visited,u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph,visited,v)

def intuse( I, x, y ):
    #wierzchołki
    T= []
    for i in range(len(I)):
        T.append(I[i][0])
        T.append(I[i][1])
    T.sort()

    indexes = [None for _ in range (T[-1]+1)]
    index = 0
    vertex = [T[0]]
    indexes[T[0]] = 0
    for i in range(1,len(T)):
        if T[i] != vertex[index]:
            index+=1
            vertex.append(T[i])
            indexes[T[i]] = index

    if indexes[x] == None or y>=len(indexes):
        return []
    if indexes[y] == None:
        return[]

    #graf
    graph_x= [[]for _ in range(len(vertex))]
    graph_y= [[]for _ in range(len(vertex))]
    for i in range(len(I)):
        graph_x[indexes[I[i][0]]].append(indexes[I[i][1]])
        graph_y[indexes[I[i][1]]].append(indexes[I[i][0]])

    #dfs
    visited_x = [False for _ in range(len(vertex))]
    visited_y = [False for _ in range(len(vertex))]
    dfs(graph_x,visited_x,indexes[x])
    dfs(graph_y,visited_y,indexes[y])

    #final result
    result = []
    for i in range(len(I)):
        if visited_x[indexes[I[i][0]]] and visited_y[indexes[I[i][1]]]:
            result.append(i)





    return result

    
runtests( intuse )


