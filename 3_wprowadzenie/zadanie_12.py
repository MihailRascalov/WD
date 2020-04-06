# Stwórz pakiet ciągi. Jeden moduł niech dotyczy działań i wzorów związanych z ciągami
# arytmetycznymi, a drugi niech dotyczy działań i wzorów związanych z ciągami geometrycznymi.

from ciagi import arithmetic_sequence, geometric_sequence

arithmetic_sequence.formula_for_the_nth_word()
print(arithmetic_sequence.formula_for_sum_nth_words_of_sequence(2, 10, 5))
print(arithmetic_sequence.sum_of_the_arithmetic_sequence())
print(arithmetic_sequence.sum_of_the_arithmetic_sequence(1, 2, 5))

geometric_sequence.formula_for_the_nth_word()
print(geometric_sequence.formula_for_sum_nth_words_of_sequence(2, 10, 5))
print(geometric_sequence.product_of_the_arithmetic_sequence())
print(geometric_sequence.product_of_the_arithmetic_sequence(1, 2, 5))