#Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.

import math

input_number = "start"

while input_number != 'q':
    input_number = input("Insert number or press \'q\' to quit: ")
    try:
        input_number = float(input_number)
        input_number = round(input_number*input_number, 2)
        print("Square = " + str(input_number))
    except ValueError:
        if(input_number=='q'):
            print("Done")
        else:
            print("Wrong data input")
    except:
        print("Another exception")