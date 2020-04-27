# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą
# operacji potęgowania oraz ilość kolejnych potęg do wygenerowania. Korzystając z funkcji
# logspace generuj tablicę jednowymiarową kolejnych potęg podanej 
# liczby, np. generuj(2,4) -> [2 4 8 16]

import numpy as np

def Generate(number, quantity):
    """Function generates one-dimensional array of successive powers of the given number"""
    return np.logspace(1, quantity+1, num=quantity, base=number, endpoint=False)

print(Generate(1, 8))
print(Generate(2, 4))
print(Generate(3, 6))
print(Generate(4, 5))
print(Generate(5, 3))