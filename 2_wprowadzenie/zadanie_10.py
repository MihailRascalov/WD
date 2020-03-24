#Napisz skrypt, który rysuje wieżę z literek. Użytkownik podaje wysokość wieży, ale nie 
#więcej jak 10.

#A
#AA
#AAA
#AAAA
#AAAAA
#AAAAAA

import sys

tower_height = input("Please insert tower height: ")

if tower_height.isdigit()==True:
    if int(tower_height) <= 10 and int(tower_height) >= 1:
        for i in range(1, int(tower_height)+1):
            for j in range(1, i+1):
                sys.stdout.write("A")
            print("")
    else:
        print("Wrong height of tower")
else:
    print("This is not a number")