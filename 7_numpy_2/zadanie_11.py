# Wygeneruj macierz płaską (wektor) i przekształć ją na macierz 3x4. Wygeneruj w ten sposób
# jeszcze kombinacje 4x3 i 2x6. Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

# Odpowiedź
#   Macierze po spłaszczeniu są identyczne

import numpy as np

vector = np.arange(0, 12)

matrix3x4 = vector.reshape(3, 4)
matrix3x4_flat = matrix3x4.ravel()

matrix4x3 = vector.reshape(4, 3)
matrix4x3_flat = matrix4x3.ravel()

matrix2x6 = vector.reshape(2, 6)
matrix2x6_flat = matrix2x6.ravel()

print(vector)

print(matrix3x4)
print(matrix4x3)
print(matrix2x6)

print(matrix3x4_flat)
print(matrix4x3_flat)
print(matrix2x6_flat)