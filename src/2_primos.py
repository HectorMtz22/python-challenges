number = input("Ingresa un número positivo: ")

def isPrime(number, isFirstTime = True):
    number = int(number)
    for i in range(2, number + 1):
        if (i == number and isFirstTime):
            return True

        if (number % i == 0):
            print(i)
            isPrime(number / i, False)
            return False
        
    return True


if (isPrime(number)):
    print("El número es primo")
else:
    print("El número no es primo")
    