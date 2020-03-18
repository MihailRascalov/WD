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

def formula_for_the_nth_word():
    print("An = a1 + (n-1) * r")
    print("An = Ak + (n-k) * r")

def formula_for_sum_nth_words_of_sequence(a1, an, n):
    return ((a1+an)/2)*n

print(formula_for_sum_nth_words_of_sequence(2,10,5))
formula_for_the_nth_word()
print(sum_of_the_arithmetic_sequence())
print(sum_of_the_arithmetic_sequence(1, 2, 5))