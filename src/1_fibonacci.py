number = input("Ingresa un número: ")

def fibonacci(number):
    newNumber = int(number)
    x1 = 0
    x2 = 1
    suma = 0
    for i in range(newNumber):
        suma = x2 + x1
        x1 = x2
        x2 = suma

    return suma
        

res = fibonacci(number)
print(res)