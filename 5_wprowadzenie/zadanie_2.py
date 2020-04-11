# Przeciąż metodę __add__() dla klasy Kwadrat, która będzie zwracała instancje klasy Kwadrat
# o nowym boku, będącym sumą boków dodawanych do siebie kwadratów.

class Ksztalty:
    """Base class for general shapes"""
    def __init__(self, x, y):
        self.x=x 
        self.y=y
        self.opis = "To będzie klasa dla ogólnych kształtów"

    def pole(self):
        """Returns square area"""
        return self.x * self.y

    def obwod(self):
        """Returns perimeter of the square"""
        return 2 * self.x + 2 * self.y

    def dodaj_opis(self, text):
        """Method allows add string to opis attribute"""
        self.opis = text

    def skalowanie(self, czynnik):
        """Method allows multiply x or y attribute by czynnik"""
        self.x = self.x * czynnik
        self.x = self.y * czynnik

class Kwadrat(Ksztalty):
    """Inheriting class from Kształty"""
    def __init__(self, x):
        self.x = x
        self.y = x

    def __add__(self, square):
        """Returns instance of Kwadrat class with new side being the sum of sides of
        Kwadrat objects added together"""
        sum = 4 * self.x + 4 * square.x
        return Kwadrat(sum)

square_00 = Kwadrat(5)
square_01 = Kwadrat(10)
result = square_00 + square_01
print(result.x)