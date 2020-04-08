# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako
# atrybut. Klasa powinna mieć metody:

# wyświetl_dane - drukuje elementy na ekran
# pobierz_elementy - pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry - pobiera pierwszą wartość i różnicę od użytkownika oraz ilośc elementów
# ciągu do wygenerowania.
# policz_sume - liczy sumę elementów
# policz_elementy - liczy elementy jeśli pierwsza wartość i różnica jest podana

# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class Arithmetic_sequence:
    """This class defines arithmetic sequences"""
    first_element = None
    increase_by_how_much = None
    how_many_elements = None

    def wyświetl_dane(self):
        """This method shows arithmetic sequence data"""
        print("First element = " + str(self.first_element))
        print("Increase by how much = " + str(self.increase_by_how_much))
        print("How many elements = " + str(self.how_many_elements))

    def pobierz_parametry(self, first_element, increase_by_how_much, how_many_elements):
        """This method gets attributes values from user for arithmetic sequence"""
        self.first_element = first_element
        self.increase_by_how_much = increase_by_how_much
        self.how_many_elements = how_many_elements

    def policz_sume(self):
        """This method calculates sum of arithmetic sequence"""
        result = ((2 * self.first_element + (self.how_many_elements - 1) * self.increase_by_how_much) / 2) * self.how_many_elements
        print(result)

    def policz_elementy(self):
        """This method shows number of elements from arithmetic sequence"""
        try:
            if self.first_element and self.increase_by_how_much:
                print("Number of elements = " + str(self.how_many_elements))
        except NameError:
            print("I don't have this data")
        except Exception as e:
            print(e)

    def pobierz_elementy(self):
        """This method gets concrete arithmetic sequence values from user"""
        list = []
        ansert = 's'
        while(ansert!='q'):
            ansert = input("Insert element of arhmetic sequence (If you are done press q): ")
            if(ansert!='q'):
                list.append(ansert)
        print("Thank you. Below is your input data." + "\n" + str(list))

first_sequence = Arithmetic_sequence()
first_sequence.pobierz_parametry(1, 2, 5)
first_sequence.wyświetl_dane()
first_sequence.policz_sume()
first_sequence.policz_elementy()
first_sequence.pobierz_elementy()