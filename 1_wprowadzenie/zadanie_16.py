#Stwórz słownik z ulubionymi grami komputerowymi. Pomyśl co może
#być kluczem, a co wartością w takim słowniku. Policz liczbę
#elementów w słowniku.

favorite_computer_games = {
    "0000-0001-68EC-0000-X-0000-0000-C" : ["Grand Theft Auto IV", 18],
    "0000-0002-68EC-0000-X-0000-0000-C" : ["The Elder Scrolls Skyrim", 18],
    "0000-0003-68EC-0000-X-0000-0000-C" : ["Battlefield IV", 18],
    "0000-0004-68EC-0000-X-0000-0000-C" : ["Towal War Rome II", 16]
}

print(favorite_computer_games["0000-0001-68EC-0000-X-0000-0000-C"][0])
print(favorite_computer_games["0000-0001-68EC-0000-X-0000-0000-C"][1])
print(favorite_computer_games["0000-0004-68EC-0000-X-0000-0000-C"][0])
print(favorite_computer_games["0000-0004-68EC-0000-X-0000-0000-C"][1])
print("Elements in dicionary = " + str(len(favorite_computer_games)))