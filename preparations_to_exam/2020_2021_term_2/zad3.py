from zad3testy import runtests


def lamps( n,T ):
    # 0 - green
    # 1 - red
    # 2 - blue
    colors = [0 for _ in range(n)]
    max_blue = 0
    tmp_blue = 0
    for i in range(len(T)):
        beg,end = T[i]
        for j in range (beg,end+1):
            if colors[j] == 0:
                colors[j] =1
            elif colors[j] == 1:
                colors[j] = 2
                tmp_blue += 1
            else:
                colors[j] = 0
                tmp_blue -=1
        max_blue = max(max_blue,tmp_blue)
    return max_blue

    
runtests( lamps )


