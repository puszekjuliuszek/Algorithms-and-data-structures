#Juliusz Wasieleski
# na samym początku ustalam dla każdego wierzchołka na którym jest poziomie
# następnie policzę ile jest wierzchołków na każdym poziomie, i wybiorę ten, który jest najszerszy
# potem, stwierdzę, które wierzchołki w drzewie muszą zostać, aby drzewo było ładne i na koniec policzę
# ile wirzchołków należy usunąć, korzystając z tego, że wiem, które muszą zostać

from builtins import len, max, range, sum
from collections import deque
from egz1btesty import runtests

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = 0       # pole do wykorzystania przez studentow

def set_levels(T):      # funkcja ustawia dla każdego wierzchołka jego poziom w drzewie
    stack = []
    T.x = 0
    stack.append((T.left,T.x))
    stack.append((T.right,T.x))
    while len(stack) >0:
        v,level = stack.pop()
        if v != None:
            v.x = level +1
            stack.append((v.left, v.x))
            stack.append((v.right, v.x))

def find_max_level(T):      # funkcja znajduje szerokość najszerszego poziomu
    max_level = 0
    stack = []
    stack.append(T.right)
    stack.append(T.left)
    while len(stack)>0:
        v = stack.pop()
        if v!=None:
            max_level = max(max_level,v.x)
            stack.append(v.right)
            stack.append(v.left)
    return max_level

def how_many_vertex(T):     # funkcja zlicza dla każdego poziomu ile na nim znajduje się  wierzchołków
    n = find_max_level(T)
    how_many = [0 for _ in range(n+1)]
    how_many[0] = 1
    stack = []
    stack.append(T.right)
    stack.append(T.left)
    while len(stack) > 0:
        v = stack.pop()
        if v != None:
            how_many[v.x] +=1
            stack.append(v.right)
            stack.append(v.left)
    return how_many

def find_best_level(how_many):      # funkcja zwraca numer poziomu, który jest najlepszy
    maxx =1
    best_level = 0
    for i in range(len(how_many)):
        if how_many[i] >= maxx:     #słaba nierówność gwarantuje, że jak znajdę lepszy poziom, który jest niżej to go wybiorę
            maxx = how_many[i]
            best_level = i
    return best_level

def which_are_necessary(T,how_many,best_level):         # funkcja ustala, które wierzchołki musimy zostawić, aby drzewo było ładne
    amount_of_vertex = sum(how_many)
    is_necessary = [[False,None] for _ in range(amount_of_vertex)]
    que = deque()
    que.append((T.left,0))
    que.append((T.right,0))
    i=0
    while que:
        v,parent = que.popleft()
        if v != None:
            i+=1
            is_necessary[i][1] = parent
            if v.x == best_level:
                is_necessary[i][0] = True
            que.append((v.left,i))
            que.append((v.right,i))

    stack =[]
    for i in range(len(is_necessary)):
        if is_necessary[i][0] == True:
            stack.append(is_necessary[i][1])

    while len(stack)>0:
        parent = stack.pop()
        if parent != None:
            is_necessary[parent][0] = True
            stack.append(is_necessary[parent][1])

    return is_necessary


def how_many_cut(T, is_necessary, how_many):      # funkcja mówi nam ile musmy usunąć krawędzi, aby zostały tylko te wierzchołki, które być muszą
    amount_of_vertex = sum(how_many)
    is_necessary = [[is_necessary[i][0],is_necessary[i][1],False] for i in range(amount_of_vertex)]
    que = deque()
    que.append((T.left, 0))
    que.append((T.right, 0))
    to_throw_away =0
    i = 0
    while que:                                  # i tak muszę przejść po całym drzewie
        v, parent = que.popleft()
        if v != None:
            i+=1
            if is_necessary[i][0]:              #jeżeli wierzchołek jest potrzebny to idę głebiej
                que.append((v.left, i))
                que.append((v.right, i))
            elif not is_necessary[parent][2]:   #jeśli jest pierwszym niepotrzebnym to doliczam krawędź idącą do niego, do licznika i oznaczam go, że on bym pierwszym, który byl niepotrzebny
                to_throw_away +=1
                is_necessary[i][2] = True
                que.append((v.left, i))
                que.append((v.right, i))
            else:                               #jak nie był potrzebny już jego rodzic, to ten automatycznie też jest wywalony, wię tylko go oznaczam i idę głębiej
                is_necessary[i][2] = True
                que.append((v.left, i))
                que.append((v.right, i))
    return to_throw_away

def wideentall( T ):
    set_levels(T)       #ustalam poziomy
    how_many = how_many_vertex(T)       #ile wierzchołków na każdym poziomie
    best_level = find_best_level(how_many)      #znajduję najlepszy poziom, aby drzewo było ładne
    is_necessary = which_are_necessary(T,how_many,best_level)       #ustalam, które wierzchołki są niezbędne
    output= how_many_cut(T,is_necessary,how_many)        # liczę ile muszę usunąć
    return output

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )