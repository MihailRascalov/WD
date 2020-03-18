#Napisz funkcję, która wykorzystuje symbol **. Funkcja ma
#przyjmować listę zakupów w postaci: klucz to nazwa produktu, a
#wartośc to ilość. Funkcja ma zliczyć ile jest wszystkich
#produktów w ogóle i zwracać tę wartość.

def add_product(** products):
    sum = 0
    for x in products:
        sum += products[x]
    return sum

print(add_product(apple=10, banana=5, onion=3, chilli_pepper=3))

