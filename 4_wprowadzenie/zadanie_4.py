#Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
#nazwa_produktu, ilość, jednostka_miary, cena_jed oraz metody
#konstruktor - który nadaje wartości
#wyświetl_produkt() - drukuje informacje o produkcie na ekranie
#ile_produktu() - informacje ile danego produktu ma być czyli ilość + jednostka_miary
#np. 1 szt., 3 kg itd.
#ile_kosztuje() - oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniakó, a cena_jed
#wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

class NaZakupy:
    """Class about some food products"""
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed
    
    def wyświetl_produkt(self):
        print(self.nazwa_produktu)
        print(self.ilosc)
        print(self.jednostka_miary)
        print(self.cena_jed)

    def ile_produktu(self):
        return self.ilosc + self.cena_jed

    def ile_kosztuje(self):
        return self.ilosc * self.cena_jed

#kurczaki, ziemniaki

chickens = NaZakupy("Chickens", 5, "kg", 19.90)
potatoes = NaZakupy("Potatoes", 50, "kg", 1)

chickens.wyświetl_produkt()
chickens.ile_kosztuje()
chickens.ile_produktu()

potatoes.wyświetl_produkt()
potatoes.ile_kosztuje()
potatoes.ile_produktu()
#test_object.wyświetl_produkt()
