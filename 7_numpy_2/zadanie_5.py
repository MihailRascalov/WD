# Utwórz macierz 2x3 różnych wartości a następnie wylicz sinus dla każdej z jej wartości
# i zapisz do zmiennej “a”.

import numpy as np

matrix = np.arange(0, 6).reshape(2, 3)
print(matrix)

a = np.sin(matrix)
print(a)