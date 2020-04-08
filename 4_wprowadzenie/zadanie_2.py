# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.

with open("numbers_divisible_by_four.txt", "r") as read_file:
    for line in read_file:
        print(line, end="")