# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku, a następnie wyświetl je
# na ekranie.

with open("writing_some_lines.txt", "w+") as write_file:
    write_file.writelines("Testing for ")
    write_file.writelines("third ")
    write_file.writelines("exercise purpose!")

with open("writing_some_lines.txt", "r") as read_file:
    for line in read_file:
        print(line)