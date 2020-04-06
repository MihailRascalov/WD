# Zdefiniuj funkcję, która oblicza długość przeciwprostokątnej, wykorzystując twierdzenie
# pitagorasa. Proszę podać wartości domyślne dla funkcji.

import math

def hypotenuse_length(a=4, b=4):
    """A function that returns the length of the hypotenuse
    a^2+b^2=c^2"""
    return math.sqrt(a**2 + b**2)

print(hypotenuse_length())
print(hypotenuse_length(6,8))