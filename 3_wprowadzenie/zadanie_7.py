#Zdefiniuj funkcję, która oblicza długość przeciwprostokątnej,
#Wykorzystując twierdzenie pitagorasa. Proszę podać wartości
#domyślne dla funkcji.

import math

def hypotenuse_length(a, b):
    return math.sqrt(a**2 + b**2)

print(hypotenuse_length(6,8))
