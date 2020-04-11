# Poczytaj o metodach __ge__, __gt__, __le__, __lt__, przeciąż je i spróbuj wykorzystać w 
# instrukcji warunkowej do porównania dwóch instancji obiektów klasy Kwadrat.

# __eq__ - obsługuje operator równości ==;
# __ne__ - obsługuje operator nierówności !=;
# __lt__ - obsługuje operator mniejsze od <;
# __gt__ - obsługuje operator większe od >;
# __le__ - obsługuje operator mniejsze równe <=;
# __ge__ - obsługuje operator większe równe >=.

from zadanie_2 import Ksztalty

class Kwadrat(Ksztalty):
    """Inheriting class from Kształty"""
    def __init__(self, x):
        self.x = x
        self.y = x
    
    def __ge__(self, square):
        """Supports operator >="""
        if self.x >= square.x:
            print("[Overload] ", end="")
            return True
        else:
            return False

    def __gt__(self, square):
        """Supports operator >"""
        if self.x > square.x:
            print("[Overload] ", end="")
            return True
        else:
            return False

    def __le__(self, square):
        """Supports operator <="""
        if self.x <= square.x:
            print("[Overload] ", end="")
            return True
        else:
            return False

    def __lt__(self, square):
        """Supports operator <"""
        if self.x < square.x:
            print("[Overload] ", end="")
            return True
        else:
            return False

square_00 = Kwadrat(10)
square_01 = Kwadrat(5)

if square_00 >= square_01:
    print("Greater or equal")
if square_00 > square_01:
    print("Greater")
if square_01 <= square_00:
    print("Less or equal")
if square_01 < square_00:
    print("Less")