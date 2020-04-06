# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe:
# Proste dane równaniami y=a1x+b1, y=a2x+b2, są
# równoległe gdy a1=a2
# prostopadłe gdy a1a2=-1

def Parallel_or_perpendicular(a1, b1, a2, b2):
    """The function checks if two lines are parallel or perpendicular
    y = a1x + b1
    y = a2x + b2
    a1 => directional coefficient of the first straight line
    b1 => free expression of the first straight line
    a2 => directional coefficient of the second straight line
    b2 => free expression of the second straight line"""
    if a1==a2:
        print("Parallel function")
    elif a1*a2==-1:
        print("Perpendicular function")
    else:
        print("Other function")

Parallel_or_perpendicular(4, 5, 4, 7)
Parallel_or_perpendicular(1, 8, -1, 2)
Parallel_or_perpendicular(2, 5, -1, 7)