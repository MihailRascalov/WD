# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego?

# Odpowiedź
#   Możliwości wygenerowania macierzy
#   1x81, 3x27, 9x9, 27x3, 81x1, 
#   ponieważ są to dzielniki liczby 81

import numpy as np

matrix = np.arange(0, 81).reshape(9, 9)
print(matrix)

matrix = np.arange(0, 81).reshape(27, 3)
print(matrix)