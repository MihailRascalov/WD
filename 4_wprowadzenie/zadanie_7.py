# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać
# współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące
# metody:

# konstruktor - który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) - metoda, która przesuwa robaczka o ile_kroków*krok w odpowiednim
# kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) - metoda, która przesuwa robaczka o ile_krokow*krok w odpowiednim
# kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) - metoda, która przesuwa robaczka o ile_krokow*krok w odpowiednim
# kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) - metoda, która przesuwa robaczka o ile_krokow*krok w odpowiednim
# kierunku i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() - metoda, która wyświetla aktualnie współrzędne Robaczka

# Stwórz instancję klasy i sprawdź jak działają wszystkie metody

class Robaczek:
    """Class controls Robaczek movement"""
    x = None
    y = None
    krok = 1

    def __init__(self, x, y, krok):
        """Constructor Robaczek type object"""
        self.x = x
        self.y = y
        self.krok = krok

    def idz_w_gore(self, ile_krokow):
        """This method moves Robaczek up by given value"""
        self.y = self.y + ile_krokow*self.krok
        return self.y

    def idz_w_dol(self, ile_krokow):
        """This method moves Robaczek down by given value"""
        self.y = self.y - ile_krokow*self.krok
        return self.y

    def idz_w_lewo(self, ile_krokow):
        """This method moves Robaczek left by given value"""
        self.x = self.x - ile_krokow*self.krok
        return self.x

    def idz_w_prawo(self, ile_krokow):
        """This method moves Robaczek right by given value"""
        self.x = self.x + ile_krokow*self.krok
        return self.x

    def pokaz_gdzie_jestes(self):
        """This method shows the current Robaczek position"""
        print("Actual position = (" + str(self.x) + ", " + str(self.y) + ")")

classic_worm = Robaczek(0,0,1)
classic_worm.pokaz_gdzie_jestes()
classic_worm.idz_w_lewo(5)
classic_worm.pokaz_gdzie_jestes()
classic_worm.idz_w_gore(10)
classic_worm.pokaz_gdzie_jestes()
classic_worm.idz_w_prawo(10)
classic_worm.pokaz_gdzie_jestes()
classic_worm.idz_w_dol(10)
classic_worm.pokaz_gdzie_jestes()
classic_worm.idz_w_lewo(5)
classic_worm.pokaz_gdzie_jestes()