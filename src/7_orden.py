def bubblesort(array):
    for i, v1 in enumerate(array):
        for j, v2 in enumerate(array):
            if (v1 < v2):
                # Cool notation for swap variables
                array[i], array[j] = array[j], array[i]
    return array

def qsort(L):
    if len(L) <= 1: return L
    return qsort([lt for lt in L[1:] if lt < L[0]]) + L[0:1] + \
           qsort([ge for ge in L[1:] if ge >= L[0]])

def welcome():
    iteraciones = input("Ingresa una cantidad\n")
    array = []
    for i in range(0, int(iteraciones)):
        value = input("Ingresa un número\n")
        array.append(int(value))
    
    return array

try:
    array = welcome()
    res = qsort(array)
    print(res)
except ValueError:
    print("Error, Try Again")
