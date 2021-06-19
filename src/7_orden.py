def bubblesort(array):
    for i, v1 in enumerate(array):
        for j, v2 in enumerate(array):
            if (v1 < v2):
                # Cool notation for swap variables
                array[i], array[j] = array[j], array[i]
    return array


def welcome():
    iteraciones = input("Ingresa una cantidad\n")
    array = []
    for i in range(0, int(iteraciones)):
        value = input("Ingresa un número\n")
        array.append(int(value))
    
    return array

try:
    array = welcome()
    res = bubblesort(array)
    print(res)
except ValueError:
    print("Error, Try Again")
