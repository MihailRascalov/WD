# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która
# będzie zawierała kolejne wartości ciągu Fibonacciego.

import numpy as np

def Fibonacci_5x5_matrix():
    matrix = np.arange(25)
    a, b = 0, 1
    for x in range(3, 26):
        a, b = b, a + b
        matrix[x-1] = b
    return matrix.reshape(5, 5)

print(Fibonacci_5x5_matrix())