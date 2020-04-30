# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

import numpy as np

matrix_one = np.arange(0, 9).reshape(3, 3)
print(matrix_one)
print(matrix_one.min(axis=1)) # rows
print(matrix_one.min(axis=0)) # columns

matrix_two = np.arange(0, 16).reshape(4, 4)
print(matrix_two)
print(matrix_two.min(axis=1))
print(matrix_two.min(axis=0))