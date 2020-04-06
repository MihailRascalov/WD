# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = ax + b
# Funkcja jest rosnąca gdy a>0
# malejąca jeżeli a<0
# stała gdy a=0
# i w zależnośći od tego będzie wyświetlać odpowiedni komunikat.

def check_monotonicity(a, b):
    """The function checks the monotonicity of the linear function
    y = ax + b
    a => directional coefficient of the straight line
    b => free expression"""
    if a > 0:
        print("Increasing function")
    elif a < 0:
        print("Descending function")
    elif a == 0:
        print("Constant function")

check_monotonicity(2, 4)
check_monotonicity(-1, 7)
check_monotonicity(0, 2)