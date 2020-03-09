#Stwórz słownik, gdzie zapiszesz imiona i nazwiska swoich znajomych
#jako klucz proszę użyć ich przezwisk (10 elementów). Następnie wyświetl
#kilka danych odwołując się do elemntów przez klucz.

friends = {
    "Rocky" : ["Sylwester", "Bostanov"],
    "Triger" : ["Marcin", "Stoski"],
    "Trash" : ["Mike", "Stris"],
    "Martini" : ["Marcel", "Labiedov"],
    "Kraxa" : ["Nikita", "Wolodniev"],
    "Pure" : ["Sonia", "Trackey"],
    "Stix" : ["Alice", "Star"],
    "Moon_boy" : ["Bartosz", "Engor"],
    "Sata" : ["Kamila", "Niepodsiad"],
    "Pirate_window" : ["Magdalena", "Czarnobylska"]
}

print(friends["Rocky"][1])
print(friends["Kraxa"][0])
print(friends["Pure"][0])
print(friends["Moon_boy"][1])
print(friends["Pirate_window"][0])