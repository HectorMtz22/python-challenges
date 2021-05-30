import random

player_value = input("Introduce un valor\n0 para piedra\n1 para papel\n2 para tijera\n")
cpu_value = int(random.random() * 3)

rules = {
    "p": 1,
}

print(rules["p"])