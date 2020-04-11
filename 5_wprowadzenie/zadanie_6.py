# Przetestuj powyższy iterator na kilku różnych kolekcjach.

class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

list_wspak = Wspak([0, 1, 2, 3, 4])
for x in list_wspak:
    print(x, end=" ")
print()

# dictionary_wspak = Wspak({"PLN": "polish_zloty", "USD": "american_dollar", "USDT": "Tether"})
# for x in dictionary_wspak:
    # print(x)

# set_wspak = Wspak({"PLN", "USD", "USDT", "ETH"})
# for x in set_wspak:
    # print(x)

tuple_wspak = Wspak((0, 2, 4, 6, 8))
for x in tuple_wspak:
    print(x, end=" ")
print()

string_wspak = Wspak("Working")
for x in string_wspak:
    print(x, end=" ")