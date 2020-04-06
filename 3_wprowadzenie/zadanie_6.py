# Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość 
# promienia. Funkcja ma przyjmować argumenty domyślne:
# Równanie okręgu dane jest wzorem:
# (x-a)^2+(y-b)^2=r^2
# gdzie (a,b) to środek okręgu, a r to promień okręgu.

import math

def radius_length(a = 0, b = 0):
    """The function returns the radius length based on the circle equation"""
    return math.sqrt(a**2 + b**2)

print(radius_length(3, 4))