from random import random

rules = {
    "r": 0,
    "p": 1,
    "t": 2
}

isInvalid = True
while (isInvalid):
    player_value = input("Introduce un valor\nr para piedra\np para papel\nt para tijera\n")
    if (player_value == "r" or player_value == "p" or player_value == "t"):
        isInvalid = False
    else:
        print("Vuelve a intentarlo")
    


cpu_value = int(random() * 3)

toPrint = ["piedra", "papel", "tijera"]

def check_winner(player, cpu):
    if (player == cpu):
        return 0
    elif (player == 2):
        if (cpu == 0):
            return -1
        else:
            return 1
    
    elif (cpu == 2):
        if (player == 0):
            return 1
        else:
            return -1
    elif (player < cpu):
        return -1
    else:
        return 1

winner = check_winner(rules[player_value], cpu_value)

if (winner == 1):
    print("Usted ganó")
    print("Jug: " + toPrint[rules[player_value]] + "\nCPU: " + toPrint[cpu_value])
elif (winner == 0):
    print("Usted empató")
    print("Jug: " + toPrint[rules[player_value]] + "\nCPU: " + toPrint[cpu_value])
else:
    print("Usted perdió")
    print("Jug: " + toPrint[rules[player_value]] + "\nCPU: " + toPrint[cpu_value])
