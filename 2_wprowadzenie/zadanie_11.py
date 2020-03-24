#Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3
#i nie więcej jak 9.

#wysokość=3
#       o
#      ooo
#       o

#wysokość równa 5
#       o
#      ooo
#     ooooo
#      ooo
#       o
#itd.

h = int(input("Please insert height of diamond <3:9>: "))

if h >= 3 and h <=9:
    for i in range(1, h, 2):
        print(" "*(h//2-i//2), "*"*i)
    for i in range(h, 0, -2):
        print(" "*(h//2-i//2), "*"*i)
else:
    print("Wrong size of diamond")