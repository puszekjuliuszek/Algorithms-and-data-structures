from zad2testy import runtests

def radix(tab):
    for i in range(len(tab)-1,-1,-1):
        tab.sort(key = lambda x: x[i])
    return tab

def ssort(L):
    maxx = max(len(L[i]) for i in range(len(L)))
    buckets = [[] for _ in range (maxx+1)]
    for word in L:
        buckets[len(word)].append(word)

    for bucket in buckets:
        radix(bucket)

    result = []
    for bucket in buckets:
        for word in bucket:
            result.append(word)
    return result

def double_prefix( L ):
    L.sort()
    result = []

    #początkowe
    j = 0
    while j < len(L[0]) and L[0][j] == L[1][j]:
        j += 1
    if L[0][0:j:] != L[2][0:j:] :
        result.append(L[0][0:j:])

    #środkowe wszystkie
    for i in range(1,len(L)-2):
        j = 0
        while j<len(L[i]) and L[i][j] == L[i+1][j]:
            j+=1
        if (L[i][0:j:] != L[i+2][0:j:] or (len(L[i])==j and L[i+1][j] != L[i+2][j])) and L[i][0:j:]!= L[i-1][0:j:]:
            result.append(L[i][0:j:])

    #ostatnie dwa
    j = 0
    while j<len(L[-2]) and L[-2][j] == L[-1][j]:
        j += 1
    result.append(L[-2][0:j:])

    result_2 = []
    for i in range(len(result)-1):
        j = 0
        while j < len(result[i]) and j < len(result[i+1]) and result[i][j] == result[i + 1][j]:
            j += 1
        if j != len(result[i]):
            result_2.append(result[i])

    result_2.append(result[-1])
    return result_2


runtests( double_prefix )


