#I link the name Floyd-Warshall with "Florida". I guess it sounds similiar. 

def Floyd_Warshall(G):
    #making matrix to hold values
    n = len(G)
    D = [[G[i][j] for j in range(n)] for i in range(n)]

    #bulin matrix to have parents
    PI = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] != float('inf') and i!=j:
                PI[i][j] = i

    #the main algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if D[i][j]> D[i][k] + D[k][j]:
                    D[i][j] = D[i][k] + D[k][j]
                    PI[i][j] = PI[k][j]
    return D,PI

def Print_all_pairs_shortest_path(PI,i,j):
    stack = []
    stack.append((i,j))
    ans = []
    while len(stack)>0:
        i , j = stack.pop()
        if  i==j:
            ans.append(i)
        elif PI[i][j] == None:
            return f"nie ma ścieżki z {i} do {j}"
        else:
            ans.append(j)
            stack.append((i,PI[i][j]))
    return ans

if __name__ == "__main__":
    inf = float('inf')
    G=[[0,3,8,inf,-4],
       [inf,0,inf,1,7],
       [inf,4,0, inf, inf],
       [2, inf,-5,0,inf],
       [inf, inf, inf, 6,0]]

    values, parents = Floyd_Warshall(G)

    print (parents)
    for i in range(len(G)):
        for j in range(len(G)):
            to_print = f" path from {i} to {j} is: {Print_all_pairs_shortest_path(parents,i,j)}"
            print(to_print)
