number = input("Ingresa un numero: ") 
base = input("Ingresa la base: ")

def residuo(number, base, iteration = 0):
    cociente = number // base
    res = number % base
    print("  " * iteration, res, cociente)

    if (cociente < base): 
        return
    else:
        return residuo(cociente, base, iteration + 1)

base = int(base)
residuo(int(number), base)
