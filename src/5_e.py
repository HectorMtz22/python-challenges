#import sys

#sys.setrecursionlimit(10**8)

# For recursion limit

def calculate_e(number):
    total = 0
    for i in range(0, number):
        formula = (1 ** i) / factorial(i)
        total += formula
    
    return total


def factorial(n, suma = 1): 
    if (n > 1):
        suma = suma * n
        return factorial(n - 1, suma) # Acuerdate siempre de retornar
    else:
        return suma

def welcome():
    number = input("Ingresa un número positivo: ")
    try:
        number = int(number)
        return calculate_e(number)

    except ValueError:
        print("La entrada es incorrecta")
        return False

print(welcome()) # Executes the program with welcome func
