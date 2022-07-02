from jeztesty import runtests
from queue import PriorityQueue

def dfs_lake(L,i,j):
    size = 0
    stack =[(i,j)]
    while len(stack) > 0:
        row,col = stack.pop()
        if L[row][col] == "W":
            L[row] = L[row][0:col:] + "L" + L[row][col+1:len(L):]
            size += 1
            if row>0:
                stack.append((row-1,col))
            if col > 0:
                stack.append((row, col-1))
            if row < len(L)-1:
                stack.append((row + 1, col))
            if col < len(L)-1:
                stack.append((row , col+1))
    return size

def djikstra_land(L):
    que = PriorityQueue()
    que.put((1,0,0))
    visited = [[False for _ in range(len(L))] for _ in range(len(L))]
    while not que.empty():
        prior,row, col = que.get()

        if row == len(L)-1 and col == len(L)-1 and L[row][col] == "L":
            return prior
        if L[row][col] == "L" and not visited[row][col]:
            visited[row][col] = True
            if row > 0:
                que.put((prior +1,row - 1, col))
            if col > 0:
                que.put((prior +1,row, col - 1))
            if row < len(L) - 1:
                que.put((prior +1,row + 1, col))
            if col < len(L) - 1:
                que.put((prior +1,row, col + 1))
    return -1

def solution(matrix):
    path = djikstra_land(matrix)
    lakes = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == "W":
                lakes.append(dfs_lake(matrix,i,j))

    if len(lakes) == 0:
        size= 0
    else:
        size = max(lakes)
    return [len(lakes), size, path]

# zmien all_tests na: 
# 0 dla pierwszego progu złożoności 
# 1 dla drugiego progu złożoności
# 2 dla wzorcowego rozwiązania
runtests(solution, all_tests = 2)