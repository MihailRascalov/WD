#Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj listę, która 
#będzie zawierała tylko elementy znajdujące się na przekątnej.

import random

matrix = [[random.randint(0,1000) for j in range(4)] for i in range(4)]
list = []

print(matrix)

for x in range(0,4):
    list.append(matrix[x][x])

print(list)