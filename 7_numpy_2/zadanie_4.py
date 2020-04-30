# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga
# liczby rzeczywiste. Następnie wykonaj na nich operację mnożenia.

import numpy as np

matrix_one = np.arange(0, 3, dtype="int64")
print(matrix_one*2)

matrix_two = np.arange(1.2, 1.7, 0.2, dtype="float")
print(matrix_two*3)