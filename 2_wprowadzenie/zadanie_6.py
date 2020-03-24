#Napisz pętle, która wyświetla liczby podzielne przez 5.

quantity = int(input("How many numbers divided by 5 show: "))

upper_range = quantity * 5 + 5

for x in range(5, upper_range, 5):
    print(str(x))