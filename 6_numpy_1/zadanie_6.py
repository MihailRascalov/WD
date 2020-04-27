# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci
# wykreślanki, gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po
# ukosie. Jedno z tych słów powinno być wypisane od prawej do lewej.

import numpy as np
import math

def word_search(column, row, diagonal):
    """Prints some words game"""
    max_size = max(len(column), len(row), len(diagonal))
    matrix = np.chararray((max_size, max_size))
    matrix[:] = "-"

    if row[-1] == column[0] and row[-1] == diagonal[0]:
        for x in range(0, max_size):
            for y in range(0, max_size):
                if x == 0:
                    matrix[0][y] = row[len(row)-1-y]
                if y == 0:
                    matrix[x][0] = column[x]
                if x == y:
                    matrix[x][y] = diagonal[x]
    print(matrix.decode("utf-8"))

column_word = "CRYPTO"
row_word = "FABRIC"
diagonal_word = "CRISIS"
word_search(column_word, row_word, diagonal_word)