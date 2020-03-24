#Napisz skrypt, ktory odczytuje liczby od użytkownika i umieszcza je na liście.
#Wykorzystaj pętle while.

print("Insert numbers, if you want to exit press q")

list = []
value_inserted = ""

while 'q'!=value_inserted:
    value_inserted = input()
    if value_inserted != 'q':
        list.append(value_inserted)
    else:
        print("Work done")
        print("Elements of list")
        for x in list:
            print(str(x))