#Napisz skrypt, który rysuje wieżę z literek. Użytkownik
#podaje wysokość nie mniej jak 3 i nie więcej jak 9
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

print("Please insert height of diamont <3:9>: ")
diamont_height = input()
if diamont_height.isdigit() and int(diamont_height)>=3 and int(diamont_height)<=9:
    print("I can draw a diamont")
    #implementation
else:
    print("Wrong height of diamont")

