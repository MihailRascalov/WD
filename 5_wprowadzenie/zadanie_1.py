# Stwórz 3 klasy: Material, Ubrania, Sweter. 

# Klasa: Material
#   Atrybuty:
#       rodzaj,
#       długość
#       szerokość

# Metody:
#   konstruktor
#   wyświetl_nazwę

# Klasa: Ubrania
#   Atrybuty:
#       rozmiar
#       kolor
#       dla_kogo

# Metody:
#   wyświetl_dane – do wyświetlania informacji o ubraniu

# klasa: Sweter
#   Atrybuty:
#       rodzaj_swetra – np. Rozpinany, z golfem itd.

# Metody:
#   wyświetl_dane

# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji
# obiektów i sprawdź, które metody można wykorzystać.

class Material:
    """Base class with four attributes, constructor and one method"""
    nazwa = "Some material"
    
    def __init__(self, rodzaj, dlugosc, szerokosc):
        """Constructor for three attributes
        dlugosc, szerokosc in cm""" 
        self.rodzaj = rodzaj
        self.dlugosc = dlugosc
        self.szerokosc = szerokosc

    def wyswietl_nazwe(self):
        """Shows information about material name"""
        print("Nazwa materialu = " + str(self.nazwa))

class Ubrania(Material):
    """Inheriting class with three attributes and one method"""
    rozmiar = None
    kolor = None
    dla_kogo = None

    def wyswietl_dane(self):
        """Shows information about cloth"""
        print("Rozmiar ubrania = " + str(self.rozmiar))
        print("Kolor ubrania = " + str(self.kolor))
        print("Dla kogo ubranie = " + str(self.dla_kogo))

class Sweter(Ubrania):
    """Inheriting class with one attribut and one method"""
    rodzaj_swetra = None

    def wyswietl_dane(self):
        """Shows information about sweater"""
        print("Sweater type = " + str(self.rodzaj_swetra))

material_000 = Material("natural", 100, 100)
material_000.nazwa = "cotton"
material_000.wyswietl_nazwe()
print()

cloth_000 = Ubrania("unnatural", 110, 70)
cloth_000.wyswietl_nazwe()
cloth_000.rozmiar = "M"
cloth_000.kolor = "Black"
cloth_000.dla_kogo = "Sasha Borysev"
cloth_000.wyswietl_dane()
print()

Sweater_000 = Sweter("natural", 80, 60)
Sweater_000.rodzaj_swetra = "cardigan"
Sweater_000.wyswietl_nazwe()
Sweater_000.wyswietl_dane()