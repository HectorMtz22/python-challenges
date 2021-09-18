import sys

sys.setrecursionlimit(10**8)

number = input("Ingresa un número: ")

def fibonacci(number):
    newNumber = int(number)
    x1 = 0
    x2 = 1
    suma = 0
    for i in range(1, newNumber):
        suma = x2 + x1
        x1 = x2
        x2 = suma

    return suma


def fibonacci_recursivo(number, actual, pasado, antepasado):
    number = int(number)
    actual = pasado + antepasado
    antepasado = pasado
    pasado = actual
    if (number <= 2):
        return actual

    return fibonacci_recursivo(number - 1, actual, pasado, antepasado)

# res = fibonacci(number)
# print(res)
        
actual = 0
pasado = 1
antepasado = 0
print(fibonacci_recursivo(number, actual, pasado, antepasado))