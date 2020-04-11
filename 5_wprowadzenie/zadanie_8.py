# Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu
# tekstowego. Zaimplementuj sprawdzanie czy przekazany został string jako argument
# konstruktora tego iteratora (sprawdź funkcję isinstance()).

class Vowel:
    """Iterator that returns vowels from string"""
    def __init__(self, data):
        self.data = data
        if isinstance(self.data, str):
            self.index = 0
            self.vowel_list = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
        else:
            print("Wrong argument type")

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            if self.data[self.index] in self.vowel_list:
                self.index = self.index + 1        
                return self.data[self.index - 1]
            else:
                self.index = self.index + 1
        else:
            raise StopIteration     

some_int = Vowel(5123321)                
string_even = Vowel("Brzęczyszczykiewicz")
for x in string_even:
    print(x, end=" ")