# Napisz funkcję, która:
    # na wejściu przyjmuje jeden parametr określający długość wektora,
    # na podstawie parametru generuje wektor, ale w kolejności odwróconej
        # (czyli np. dla n=3 =>[3 2 1])
    # generuje macierz diagonalną z w/w wektorem jako przekątną

import numpy as np

def diagonal_matrix(vector_length):
    """Function returns diagonal matrix with vector as a diagonal"""
    return np.diag([a for a in range(vector_length, 0, -1)])

print(diagonal_matrix(5))