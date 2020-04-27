# Napisz funkcję, która:
    # jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr
        #  ‘kierunek’,
    # parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
    # funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat, że
    # ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)

import numpy as np

def Divide_the_matrix_in_half(matrix_to_divide, direction):
    """Divides matrix in half if it is possible
    direction("|") => vertically
    direction("-") => horizontally"""
    if direction == "|":
        if matrix_to_divide.shape[1] % 2 == 0:
            n = int(matrix_to_divide.shape[1] / 2)
            return (matrix_to_divide[:, :n])
        else:
            return "You can't divide matrix in half vertically. Wrong number of columns."
    elif direction == "-":
        if matrix_to_divide.shape[0] % 2 == 0:
            n = int(matrix_to_divide.shape[0] / 2)
            return (matrix_to_divide[:n, :])
        else:
            return "You can't divide matrix in half horizontally. Wrong number of rows."
    else:
        return "Wrong direction."

matrix = np.arange(0, 12).reshape(3, 4)
print(matrix)
print(Divide_the_matrix_in_half(matrix, "|"))
print(Divide_the_matrix_in_half(matrix, "-"))
print(Divide_the_matrix_in_half(matrix, "x"))

matrix2 = matrix.reshape(4, 3)
print(matrix2)
print(Divide_the_matrix_in_half(matrix2, "|"))
print(Divide_the_matrix_in_half(matrix2, "-"))