def factorial(n):
    suma = 1
    for i in range(n, 1, -1):
        suma = suma * i
    
    return suma

def triangulo(n, k):
    temp_n = factorial(n)
    temp_n_k = factorial(n - k)
    temp_k = factorial(k)
    formula = temp_n / (temp_n_k * temp_k)
    return formula

values = triangulo(31, 5)
print(values)