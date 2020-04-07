# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako
# atrybut. Klasa powinna mieć metody:

# wyświetl_dane - drukuje elementy na ekran
# pobierz_elementy - pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry - pobiera pierwszą wartość i różnice od użytkownika oraz ilośc elementów
# ciągu do wygenerowania.
# policz_sume - liczy sumę elementów
# policz_elementy - liczy elementy jeśli pierwsza wartość i różnica jest podana

#Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Arithmetic_sequence:
    """This class defines arithmetic sequences"""
    def __init__(self, first_element, increase_by_how_much, how_many_elements):
        self.first_element = first_element
        self.increase_by_how_much = increase_by_how_much
        self.how_many_elements = how_many_elements

    def show_arithmetic_sequence_data(self):
        print("First element = " + str(self.first_element))
        print("Increase by how much = " + str(self.increase_by_how_much))
        print("How many elements = " + str(self.how_many_elements))

first_sequence = Arithmetic_sequence(1,2,5)
first_sequence.show_arithmetic_sequence_data()