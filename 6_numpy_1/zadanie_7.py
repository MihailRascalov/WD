# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:

# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]

# Przy założeniach:
    # funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza
    # wielokrotność liczby 2 na kolejnych jej przekątnych rozchodzących się od głównej
    # przekątnej.

import numpy as np

def Generate_multidimensional_matrix(n):
    """Function generates multidimensional matrix size n*n"""
    matrix = np.diag([2 for a in range(n)])
    shift = 4
    for x in range(1, n):
        matrix += np.diag([shift for a in range(n-x)], x)
        matrix += np.diag([shift for a in range(n-x)], -x)
        shift += 2
    print(matrix)

Generate_multidimensional_matrix(2)
Generate_multidimensional_matrix(3)
Generate_multidimensional_matrix(4)
Generate_multidimensional_matrix(5)