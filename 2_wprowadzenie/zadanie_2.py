#Napisz skrypt, który pobiera od użytkownika dwie wartości i mnoży je przez siebie.
#Wynik wyświetla na ekranie. (użyj instrukcji readline() i write())

print("Insert two numbers")
first_value = input("Insert first value\n")
second_value = input("Insert second value\n")
first_value = float(first_value)
second_value = float(second_value)
result = round(first_value*second_value, 2)

print("Result = " + str(result))