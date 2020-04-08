# Stwórz klasę NaZakupy, która będzie przechowywać atrybuty: nazwa_produktu, ilosc,
# jednostka_miary, cena_jed oraz metody: konstruktor - który nadaje wartości 
# wyświetl_produkt() - drukuje informacje o produkcie na ekranie ile_produktu() - informacje 
# ile danego produktu ma być czyli ilość + jednostka_miary np. 1 szt., 3 kg itd. 
# ile_kosztuje() - oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków, a cena_jed 
# wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2.

class NaZakupy:
    """Class that allows us use three methods
    wyświetl_produkt => Shows information about product
    ile_produktu => Return quantity of product
    ile_kosztuje => Return price of product"""
    nazwa_produktu = None
    ilosc = None
    jednostka_miary = None
    cena_jed = None
    
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        """Constructor with four variables creates object"""
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    
    def wyświetl_produkt(self):
        """Method shows all atributes of object"""
        print(self.nazwa_produktu, end=" ")
        print(self.ilosc, end="")
        print(self.jednostka_miary, end=" ")
        print(str(self.cena_jed) + "zł/" + str(self.jednostka_miary))

    def ile_produktu(self):
        """Method shows quantity of product"""
        print("How much = " + str(self.ilosc) + str(self.jednostka_miary) + " " +
                str(self.nazwa_produktu))

    def ile_kosztuje(self):
        """Method shows price of product"""
        print(str(self.nazwa_produktu) + " price = " + str(self.ilosc * self.cena_jed) + "zl")

chicken = NaZakupy("Chicken", 5, "kg", 19.90)
potatoe = NaZakupy("Potatoe", 50, "kg", 1)

chicken.wyświetl_produkt()
chicken.ile_produktu()
chicken.ile_kosztuje()

potatoe.wyświetl_produkt()
potatoe.ile_produktu()
potatoe.ile_kosztuje()