from zad1testy import runtests

def lds(T,n):
    DP = [[1, None] for i in range(n)]
    for i in range(n):
        for j in range(i):
            if T[i] < T[j] and DP[j][0] <= DP[i][0]:
                DP[i][0] = DP[j][0] + 1
                DP[i][1] = j

    max_ind = None
    maxx = 1
    for i in range(len(DP)):
        if DP[i][0] > maxx:
            maxx = DP[i][0]
            max_ind = i

    result = []
    while max_ind != None:
        result.append(T[max_ind])
        max_ind = DP[max_ind][1]
    result.reverse()
    return result

def lis(T,n):
    DP = [[1,None] for i in range(len(T))]
    for i in range(n,len(T)):
        for j in range(n,i):
            if T[i]>T[j] and DP[j][0]>=DP[i][0]:
                DP[i][0] = DP[j][0]+1
                DP[i][1] = j

    max_ind = None
    maxx = 1
    for i in range(len(DP)):
        if DP[i][0]>maxx:
            maxx = DP[i][0]
            max_ind = i

    result = []
    while max_ind != None:
        result.append(T[max_ind])
        max_ind = DP[max_ind][1]
    result.reverse()
    return result

def mr( X ):
    maxx = 0
    max_ind = 0
    for i in range(len(X)+1):
        if len(lds(X,i))+ len(lis(X,i))>maxx:
            maxx = len(lds(X,i))+ len(lis(X,i))
            max_ind = i

    res = lds(X,max_ind) + lis(X,max_ind)
    return res

    
runtests( mr )


