number = input("Ingresa un número positivo: ")

def isPrime(number):
    number = int(number)
    for i in range(2, number):
        if (number % i == 0):
            return False
        

    return True

if (isPrime(number)):
    print("El número es primo")
else:
    print("El número no es primo")
    