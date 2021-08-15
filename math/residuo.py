number = input("Ingresa un numero: ") 
base = input("Ingresa la base: ")

def residuo(number, base):
    cociente = number // base
    print("Cociente:", cociente)
    res = number % base
    print("Residuo:", res)
    return

residuo(int(number), int(base))
