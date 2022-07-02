from adotesty import runtests
from math import log10


def brut(n,m):



    for _ in range(m):
        n_tmp = n
        n_new = n_tmp % 10 + 1

        n_tmp //= 10
        while n_tmp >0:
            digit = n_tmp%10 +1
            n_new += digit*(10**int(log10(n_new)+1))
            n_tmp //= 10
        n = n_new

    return n


def function(n, m):
    # Tutaj wprowadź kod
    return int(log10(brut(n,m)))+1


# zmien all_tests na: 
# 0 dla pierwszego progu złożoności 
# 1 dla drugiego progu złożoności
# 2 dla wzorcowego rozwiązania
runtests(function, all_tests = 0)
