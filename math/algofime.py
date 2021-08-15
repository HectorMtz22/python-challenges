number = input("Ingresa el número: ")
base = input("Ingresa la base: ")

def multiply(number, base):
    for i in number:
        temp = int(i, base)
        print(temp)


multiply(number, int(base))
