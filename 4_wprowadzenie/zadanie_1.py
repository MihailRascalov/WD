#Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.

import sys

word_counter = 0
with open("numbers_divisible_by_four.txt", "w") as write_file:
    for x in range(4, 4001, 4):
        if(word_counter<10):
            write_file.write(str(x) + " ")
            word_counter += 1
        else:
            write_file.write("\n")
            word_counter = 0