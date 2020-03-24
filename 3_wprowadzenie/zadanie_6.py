#Zdefiniuj funkcję, która na podstawie równania okręgu w postaci kanonicznej zwróci długość 
#promienia. Funkcja ma przyjmować argumenty domyślne:
#Równanie okręgu dane jest wzorem:
#(x-a)^2+(y-b)^2=r^2
#gdzie (a,b) to środek okręgu, a r to promień okręgu.

import math

def radius_length(a = 0, b = 0):
    result = a**2 + b**2
    return math.sqrt(result)

print(radius_length(3, 4))
