from zad2testy import runtests

def ssort(L):
    maxx = max(len(L[i]) for i in range(len(L)))
    return maxx

def double_prefix( L ):
    """tu prosze wpisac wlasna implementacje"""

    return ssort(L)


runtests( double_prefix )

