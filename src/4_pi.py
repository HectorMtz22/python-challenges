def calculate_pi(n):
    sum = 0
    for i in range(0, n):
        formula = ((4/(8 * i + 1)) - (2/(8 * i + 4)) - (1/(8 * i + 5)) - (1/(8 * i + 6)))  * ((1/16)**i)
        sum += formula
    
    return sum


# Init of program
cifra_pi = input("Introduce una cifra para calcular pi con precisión\n")
try:
    total = calculate_pi(int(cifra_pi)) # Call the function
    print("Pi is", total) # Print results
except ValueError:
    print("Invalid entries!") # If sth wents wrong