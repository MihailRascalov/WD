# Za pomocą funkcji isinstance() oraz issubclass() sprawdź wynik dla instancji obiektu
# Pracownik oraz Menadzer dla klas Osoba, Pracownik i Manadzer.

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):
    
    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


jozek = Pracownik("Józek", "Bajka", 2000)
adrian = Menadzer("Adrian", "Mikulski", 12000)

print(isinstance(jozek, Osoba))
print(isinstance(jozek, Pracownik))
print(isinstance(jozek, Menadzer))
print(isinstance(adrian, Osoba))
print(isinstance(adrian, Pracownik))
print(str(isinstance(adrian, Menadzer)) + "\n")

print(issubclass(Pracownik, Osoba))
print(issubclass(Menadzer, Osoba))
print(issubclass(Osoba, Pracownik))
print(issubclass(Menadzer, Pracownik))
print(issubclass(Osoba, Menadzer))
print(issubclass(Pracownik, Menadzer))