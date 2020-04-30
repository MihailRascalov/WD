# Utwórz nową macierz 2x3 różnych wartości a następnie wylicz cosinus dla każdej z jej 
# wartości i zapisz do zmiennej “b”.

import numpy as np

matrix = np.arange(2, 8).reshape(2, 3)
print(matrix)

b = np.cos(matrix)
print(b)