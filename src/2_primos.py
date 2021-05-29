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

def welcome():
    number = input("Ingresa un número positivo: ")
    try:
        number = int(number)
        if (number < 0):
            print("la entrada debe ser positiva")
            return False
        if (isPrime(number)):
            print("El número es primo")
        else:
            print("El número no es primo")
    
        return True

    except ValueError:
        print("La entrada es incorrecta")
        return False

loop = True
while(loop):
    valor = welcome()
    if valor:
        loop = False
