#Napisz pętle, która pobiera liczby od
#użytkownika i wyświetla ich
#kwadraty na ekranie.
import math

input_number = "start"
while input_number != 'q':
    print("Insert number or press \'q\' to quit")
    input_number = input()
    try:
        input_number = float(input_number)
        if (input_number >= 0.0 or input_number <= 0.0):
            print("Square = " + str(round(math.sqrt(input_number), 2)))
    except ValueError:
        print("Wrong data input")
    except:
        print("Some general exception")