#Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry.
#Wynik wyświetla na ekranie. Wykorzystaj pętle while.

print("Enter a multi-digit number (example 37125): ")

number = input()
sum = 0

if number.isdigit() == True:
    number_length = len(number)
    for x in number:
        sum += int(x)
else:
    print("This is not a number")

print("Sum of input multi-digit number = " + str(sum))