# Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów
# przekazanej kolekcji.

class Even:
    """Iterator that returns even values"""
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.end = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            if self.index % 2 == 0:    
                self.index = self.index + 1        
                return self.data[self.index - 1]
            else:
                self.index = self.index + 1        
        else:
            raise StopIteration

list_even = Even([0, 1, 2, 3, 4])
for x in list_even:
    print(x, end=" ")
print()

# dictionary_even = Even({"PLN": "polish_zloty", "USD": "american_dollar", "USDT": "Tether"})
# for x in dictionary_even:
    # print(x)

# set_even = Even({"PLN", "USD", "USDT", "ETH"})
# for x in set_even:
    # print(x)

tuple_even = Even((0, 2, 4, 6, 8))
for x in tuple_even:
    print(x, end=" ")
print()

string_even = Even("Working")
for x in string_even:
    print(x, end=" ")