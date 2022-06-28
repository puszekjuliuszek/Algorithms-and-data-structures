from zad2testy import runtests
from queue import PriorityQueue

def go_further(direction,que,prior,moves,dist,x,y,dx,dy,dir):
    if dir == direction:
        que.put((prior + moves[dist][0], x +dx, y+dy, direction, moves[dist][1]))
    elif dir == (direction + 2) % 4:
        que.put((prior + 90 + 60, x +dx, y+dy, direction, 1))
    else:
        que.put((prior + 45 + 60, x +dx, y+dy, direction, 1))

def robot(L, A, B):
    visited = [[False for _ in range(len(L[0]))] for _ in range(len(L))]
    for i in range(len(L)):
        for j in range(len(L[0])):
            if L[i][j] == "X":
                visited[i][j] = True
    que = PriorityQueue()
    moves = ((60,1),(40,2),(30,2))
    mindist = float('inf')
    que.put((0,A[1],A[0],2,0))

    while not que.empty():
        prior,x,y,dir,dist = que.get()

        if x == B[1] and y == B[0]:
            mindist = min(mindist,prior)

        if not visited[x - 1][y]:
            go_further(1, que, prior, moves, dist, x, y, -1, 0,dir)

        if not visited[x + 1][y]:
            go_further(3, que, prior, moves, dist, x, y, 1, 0,dir)

        if not visited[x ][y+1]:
            go_further(2, que, prior, moves, dist, x, y, 0, 1,dir)

        if not visited[x][y-1]:
            go_further(0, que, prior, moves, dist, x, y, 0, -1,dir)

        visited[x][y] = True
    
    if mindist<float('inf'):
        return mindist
    else:
        return None

runtests(robot)

