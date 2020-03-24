#Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe:
#Proste dane równaniami y=a1x+b1, y=a2x+b2, są
#równoległe gdy a1=a2
#prostopadłe gdy a1a2=-1

def Parallel_or_perpendicular(a1, b1, a2, b2):
    if a1==a2:
        print("Parallel function")
    elif a1*a2==-1:
        print("Perpendicular function")
    else:
        print("Other function")

Parallel_or_perpendicular(2, 5, -1, 7)