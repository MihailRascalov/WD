#Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu
#arytmertcznego.

#Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa),
#r(wielkość o ile rosną kolejne elementy) i ile_ilementów (ile 
# elementów ma sumować). Ponadto funkcja niech przyjmuje wartości
#domyślne: a1=1, r=1, ile=10

def sum_of_the_arithmetic_sequence(a1 = 1, r = 1,
    how_many_elements = 10):
    if how_many_elements == 1:
        return a1
    elif how_many_elements == 0:
        return 0.0
    
    sum = a1
    sum_sequence = a1
    for i in range(1, how_many_elements):
        sum += r
        sum_sequence += sum
    return sum_sequence
print(sum_of_the_arithmetic_sequence())
print(sum_of_the_arithmetic_sequence(1, 2, 5))