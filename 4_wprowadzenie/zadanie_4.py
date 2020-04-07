# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty: nazwa_produktu, ilość,
# jednostka_miary, cena_jed oraz metody konstruktor - który nadaje wartości wyświetl_produkt()
# - drukuje informacje o produkcie na ekranie ile_produktu() - informacje ile danego produktu
# ma być czyli ilość + jednostka_miary np. 1 szt., 3 kg itd. ile_kosztuje() - oblicza ile
# kosztuje dana ilość produktu np. 3 kg ziemniakó, a cena_jed wynosi 2 zł/kg wówczas funkcja
# powinna zwrócić wartość 3*2

class NaZakupy:
    """Class that allows use of four methods
    wyświetl_produkt => information about product
    ile_produktu => how much product
    ile_kosztuje => return price of product"""
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    
    def wyświetl_produkt(self):
        print(self.nazwa_produktu, end=" ")
        print(self.ilosc, end="")
        print(self.jednostka_miary, end=" ")
        print(str(self.cena_jed) + "/" + str(self.jednostka_miary))

    def ile_produktu(self):
        print("How much = " + str(self.ilosc) + str(self.jednostka_miary) + " " + str(self.nazwa_produktu))

    def ile_kosztuje(self):
        print(str(self.nazwa_produktu) + " price = " + str(self.ilosc * self.cena_jed) + "zl")

chicken = NaZakupy("Chicken", 5, "kg", 19.90)
potatoe = NaZakupy("Potatoe", 50, "kg", 1)

chicken.wyświetl_produkt()
chicken.ile_produktu()
chicken.ile_kosztuje()

potatoe.wyświetl_produkt()
potatoe.ile_produktu()
potatoe.ile_kosztuje()