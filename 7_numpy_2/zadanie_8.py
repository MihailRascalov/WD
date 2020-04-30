# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

import numpy as np

matrix = np.arange(9).reshape(3,3)
print(matrix)

for a in matrix:
   print("\n" + str(a))
print()