def calculate_e(number):
    return 


def factorial(n, suma): 
    if (n > 1):
        suma = suma * n
        return factorial(n - 1, suma) # Acuerdate siempre de retornar
    else:
        return suma


print(factorial(8, 1))