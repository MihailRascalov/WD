# Utwórz słownik z produktami spożywczymi do kupienia. Klucz to niech będzie nazwa produktu, a 
# wartość - jednostka w jakiej się je kupuje (np. sztuki, kg itd.). Wykorzystaj Python
# Comprehension do zdefiniowania nowej listy, gdzie będą produkty, których wartość to sztuki.

groceries = {"mleko": "sztuki",
             "banany": "kilogramy",
             "pomidory": "kilogramy",
             "płatki owsiane": "sztuki",
             "chleb": "sztuki"
             }

set_values = {k for (k,v) in groceries.items() if v == "sztuki"}
print(list(set_values))