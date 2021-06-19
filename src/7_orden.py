def bubblesort(array):
    for i, v1 in enumerate(array):
        for j, v2 in enumerate(array):
            if (v1 < v2):
                # Cool notation for swap variables
                array[i], array[j] = array[j], array[i]
    return array


res = bubblesort([1, 4, 32, 2, 5])
print(res)