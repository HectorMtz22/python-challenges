def calculate_pi(number):
    sum = 0
    for i in range(0, number):
        formula = ((4/(8 * i + 1)) - (2/(8 * i + 4)) - (1/(8 * i + 5)) - (1/(8 * i + 6)))  * ((1/16)**i)
        sum += formula
    
    return sum


total = calculate_pi(10)
print(total)