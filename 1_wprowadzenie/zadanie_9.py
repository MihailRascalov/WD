#Napisz skrypt, w którym zadeklarujesz zmienne typu: string, float i szestnastkowe. 
#Następnie wyświetl je wykorzystując odpowiednie formatowanie.

name = "Mike"
velocity = 132.65
adress = "3b6d"

print("String variable = {0:s}".format(name))
print("Float variable = {0:f}".format(velocity))
print("Hexadecimal variable = " + str(adress))