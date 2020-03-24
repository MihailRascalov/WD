#Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. Wynik wyświetla
#na ekranie. (użyj instrukcji input)

sentence = input("Insert some sentence\n")
counter = 0

for x in sentence:
    if x == " ":
       counter += 1

print("Number of space in sentence = " + str(counter))