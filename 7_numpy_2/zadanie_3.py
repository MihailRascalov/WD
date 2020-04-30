# Wykorzystaj macierze z zadania pierwszego i wykonaj iloczyn macierzy.

import numpy as np

matrix_one = np.arange(0, 3)
matrix_one *= 2

matrix_two = np.arange(3, 6)
matrix_two *= 3

print(np.dot(matrix_one, matrix_two))