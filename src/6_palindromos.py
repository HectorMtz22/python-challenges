def palindroma(word, i, j):
    if (j < i):
        return 1

    if (word[i] == word[j] and not (i == j) and not (j < i)):
        return palindroma(word, i + 1, j - 1)
    elif (i == j and not (j < i)):
        return 1
    else:
        return 0
    return 1

word = input("Escribe una palabra\n")
res = palindroma(word, 0, len(word) - 1)

if (res):
    print("La palabra es palíndroma")
else:
    print("La palabra no es palíndroma")