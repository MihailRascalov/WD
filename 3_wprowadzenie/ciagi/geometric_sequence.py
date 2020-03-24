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

def formula_for_the_nth_word():
    print("An = a1 * q^(n-1)")
    print("An = Ak * q^(n-k)")

def formula_for_sum_nth_words_of_sequence(a1, q, n):
    if q != 1:
        return round(a1 * (1-q^(n))/(1-q), 2)
    elif q == 1:
        return round(a1 * n, 2)

print(formula_for_sum_nth_words_of_sequence(2,10,5))
formula_for_the_nth_word()
print(product_of_the_arithmetic_sequence())
print(product_of_the_arithmetic_sequence(1, 2, 5))