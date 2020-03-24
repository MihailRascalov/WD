#Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów 
#ciągu.

def product_of_the_arithmetic_sequence(a1 = 1, r = 1, how_many_elements = 10):
    if how_many_elements == 1:
        return a1
    elif how_many_elements == 0:
        return 0.0
    
    sum = a1
    list = [a1]

    for i in range(1, how_many_elements):
        sum += r
        list.append(sum)

    result = 1

    for x in list: 
         result = result * x  

    return result

print(product_of_the_arithmetic_sequence())
print(product_of_the_arithmetic_sequence(1, 2, 5))