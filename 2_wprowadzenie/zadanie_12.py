#Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100.

import sys

for i in range(1, 11):
    for j in range(1, 11):
        result = int(i)*int(j)
        sys.stdout.write((str(result) + "\t"))
    print("")