number = input("Ingresa un número: ")

def binomial_theorem(number):
    for i in range(0, number + 1):
        print("( x", i, "+",  "y", number - i, ")")

binomial_theorem(int(number))