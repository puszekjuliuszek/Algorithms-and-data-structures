#Juliusz Wasieleski

#napisałem algorytm zachłanny, bo jestem nie potrafię dokończyć mojej ideii dynamika
# ten zachłanny bierze mi największą kupę śniegu i jedzie do niej od tej strony gdzie jest mniej

# a gdybym chciał to jednak zrobić dynamicznie:
# liczbyłbym dla danego pola czy lepiej jest z niego wziąć i sprawdzić funkcją, ile byśmy we wcześniejsze dni mogli wziąć
# z pól po lewej i po prawej i wziąć maxa z tych dwóch wartości, albo nie brać i przez d dni możemy zbierać z pól po lewej i po prawej

# zrobiłbym funkcję f(d,i,s)  gdzie d to ilość dni od początku zbierania, i to pole do którego zbeiraliśmy, a s to kierunek z którego zbieramy tego dnia
#S[d][i] informauje nas ile zostało śniegu na i-tym polu po d dniach
#zatem funcka nasza zwracałaby maksymalną ilosć śniegu jaką jesteśmy w stanie uzbierać przez d dni, dojeżdżając do i-tego pola
# jadąc tego d-tego dnia od story s, gdzie s == 0 to zachód, a s == 1 to wschód

#f(d,i,s) = max{ S[d][i] + max( f(d-1,i-1,0),f(d-1, n-i +1,1 ),     max( f(d,i-1, 0), f(d,n-i+1,1) )}

from builtins import range, len, max, sum


from egz1atesty import runtests

# def snow( S ):
#     max_d = max(S)
#     new_S = [[0 for _ in range(len(S))] for _ in range(max_d)]
#     for i in range(len(S)):
#         new_S[0][i] = S[i]
#     for i in range(1,max_d):
#         for j in range(len(S)):
#             new_S[i][j] = max(new_S[i-1][j] -1,0)
#
#     return -1

def snow(S):

    amount = 0

    max_snow = 0
    max_snow_id = None
    for i in range(len(S)):
        if max_snow< S[i]:
            max_snow = S[i]
            max_snow_id = i

    while max_snow_id != None:
        amount += max_snow
        for i in range(len(S)):
            S[i] = max(S[i] - 1,0)
        left = sum(S[0:max_snow_id])
        right = sum(S[max_snow_id +1:])
        if left<right :
            for i in range(max_snow_id+1):
                S[i] = 0
        else:
            for i in range(max_snow_id, len(S)):
                S[i] = 0

        max_snow = 0
        max_snow_id = None
        for i in range(len(S)):
            if max_snow < S[i]:
                max_snow = S[i]
                max_snow_id = i

    return amount





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
