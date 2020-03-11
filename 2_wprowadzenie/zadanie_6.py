#Napisz pętle, która wyświetla liczby
#podzielne przez 5

quantity = input("How many numbers divided by 5 print: ")
quantity = int(quantity)
quantity = quantity * 5 + 5
for x in range(5, quantity, 5):
    print(str(x))
