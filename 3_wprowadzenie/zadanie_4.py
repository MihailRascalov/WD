#Zdefiniuj funkcję, która będzie badać monotoniczność funkcji
#liniowej:
#y = ax + b
#Funkcja jest rosnąca gdy a>0
#malejąca jeżeli a<0
#stała gdy a=0
#i w zależnośći od tego będzie wyświetlać odpowiedni komunikat

def check_monotonicity(a, b):
    if a > 0:
        print("Increasing function")
    elif a < 0:
        print("Descending function")
    elif a == 0:
        print("Constant function")
