# Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.

from zadanie_7 import Robaczek

class Nowy_robaczek(Robaczek):
    """Class controls Nowy_robaczek movement extended by __del__ method
    class inherits from Robaczek"""

    def __del__(self):
        """Method removes instance of object"""
        print("Object destroyed")
        
class test_class():
    """Class for testing purpose"""

    def __del__(self):
        """Method removes instance of object"""
        print("Object deleted")

another_worm = Nowy_robaczek(0, 0, 2)
another_worm.pokaz_gdzie_jestes()
another_worm.idz_w_gore(1)
another_worm.pokaz_gdzie_jestes()
another_worm.idz_w_gore(2)
another_worm.pokaz_gdzie_jestes()
another_worm.idz_w_gore(3)
another_worm.pokaz_gdzie_jestes()
another_worm.idz_w_dol(25)
another_worm.pokaz_gdzie_jestes()
print(another_worm)
del another_worm

another_worm = test_class()
print(another_worm)
del another_worm