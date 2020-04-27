# Napisz funkcję, która będzie:
    # przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
    # zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

import numpy as np

def nArray(n):
    """function returns n*n shape array"""
    table = np.ones((n,n), dtype="int64")
    counter = 1
    for x in range(0, n):
        for y in range(0, n):
            table[x][y] = counter
            counter += 1
    return table

print(nArray(9))