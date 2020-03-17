#Napisz skrypt, który liczy pierwiastek z liczby podanej
#przez użytkownika jeśli użytkownik poda wartość
#ujemną to powinien być wyłapany błąd

import math

number_to_square = int(input("Please insert number to square: "))
if number_to_square<0:
    print("Wrong number")
else:
    print("Result = " + str(round(math.sqrt(number_to_square), 2)))