# Stwórz pakiet liczby zespolone z dwoma modułami. Jeden moduł ma zawierać dwie funkcje, 
# które z podanej liczby zespolonej zwracają część rzeczywistą i część urojoną. Drugi moduł
# ma wykonywać dodawanie i odejmowanie dwóch liczb zespolonych. Przetestuj działanie 
# tego pakietu.

from liczby_zespolone import complex_numbers_one, complex_numbers_two

print(complex_numbers_one.get_real_value(4, 3))
print(complex_numbers_one.get_imag_value(4, 7))
print(complex_numbers_two.add_complex_numbers(3, 2, 1, 4))
print(complex_numbers_two.subtract_complex_numbers(4, 5, 3, 2))