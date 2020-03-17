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

#print("Please insert height of diamont <3:9>: ")
#diamont_height = input()
#if diamont_height.isdigit() and int(diamont_height)>=3 and int(diamont_height)<=9:
    #for i in range(1, diamont_height):
        #for j in range(1, diamont_height):
            #if 
#else:
    #print("Wrong height of diamont")

h = int(input("Please insert height of diamont <3:9>: "))

for i in range(1, h, 2):
    print(" "*(h//2-i//2), "*"*i)
for i in range(h, 0, -2):
    print(" "*(h//2-i//2), "*"*i)