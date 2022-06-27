from zad2testy import runtests
from queue import PriorityQueue


def robot(L, A, B):
    n = len(L)*len(L[0])
    visited = [False for _ in range(n)]
    que = PriorityQueue()
    #priorytet, x, y, kierunek, ile już

    que.put((0,A[0],A[1],0,0))
    while not que.empty():
        prior,x,y,dir,dist = que.get()
        direction = 1
        


    return 0


runtests(robot)
