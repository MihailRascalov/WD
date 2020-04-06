def sum_of_the_arithmetic_sequence(a1 = 1, r = 1, how_many_elements = 10):
    """The function returns the sum of any arithmetic string
    a1 => initial value
    r => the amount by which the next elements grow
    ile_elementów => how many items to sum"""
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
    """Listing two formulas for the nth word"""
    print("An = a1 + (n-1) * r")
    print("An = Ak + (n-k) * r")

def formula_for_sum_nth_words_of_sequence(a1, an, n):
    """The function returns the sum of nth words of sequence"""
    return ((a1+an)/2)*n