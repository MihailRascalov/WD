# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna
# przechowywać przynajmniej dwa słowa i metody:

# sprawdz_czy_palindrom - metoda sprawdza czy dany wyraz jest palindromem (czytany od
# początku czy wspak jest taki sam np. kajak)
# sprawdz_czy_metagramy - metoda sprawdza czy wyrazy różnią się jedną literą, a poza tym
# są takie same np. mata, tata.
# sprawdz_czy_anagramy - metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# wyświetl_wyrazy - wyświetla podane wyrazy

# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Slowa:
    """Class with word games methods"""
    first_word = None
    second_word = None

    def sprawdz_czy_palindrom(self, word):
        """Method checks if word is palindrome
        returns bool type
        example => kajak"""
        self.first_word = word
        tmp_string = word.upper()
        tmp_string_reversed = reversed(tmp_string)
        if list(tmp_string)==list(tmp_string_reversed):
            return True
        else:
            return False

    def sprawdz_czy_metagramy(self, word_one, word_two):
        """the method checks if the words differ one letter and rest are the same
        returns bool type
        example => mata, tata"""
        self.first_word = word_one
        self.second_word = word_two
        number_of_difference = 0
        if len(word_one)==len(word_two):
            for i in range(0, len(word_one)):
                if number_of_difference > 1:
                    return False
                if word_one[i] != word_two[i]:
                    number_of_difference += 1
            if number_of_difference == 1:
                return True
            else:
                return False
        else:
            return False

    def sprawdz_czy_anagramy(self, word_one, word_two):
        """the method checks if the words have the same set of letters
        returns bool type
        example => mata, tama"""
        self.first_word = word_one
        self.second_word = word_two
        return sorted(word_one) == sorted(word_two)

    def wyświetl_wyrazy(self):
        """Displays the given words"""
        print(self.first_word)
        print(self.second_word)

example = Slowa()
print(example.sprawdz_czy_palindrom("kajak"))
print(example.sprawdz_czy_palindrom("omen"))
print(example.sprawdz_czy_palindrom("anna"))
example.wyświetl_wyrazy()

example2 = Slowa()
print(example2.sprawdz_czy_metagramy("XRP", "ETN"))
print(example2.sprawdz_czy_metagramy("bitcoin", "litcoin"))
print(example2.sprawdz_czy_metagramy("mata", "tata"))
example2.wyświetl_wyrazy()

example3 = Slowa()
print(example3.sprawdz_czy_anagramy("mata", "tama"))
print(example3.sprawdz_czy_anagramy("usdt", "usdh"))
print(example3.sprawdz_czy_anagramy("lol", "olo"))
example3.wyświetl_wyrazy()