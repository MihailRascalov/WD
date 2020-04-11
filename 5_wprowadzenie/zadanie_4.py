# Korzystając z powyższego kodu stwórz kilka instancji klasy Point i spróbuj odwołać się do
# zmiennej counter z poziomu różnych instancji, porównując jej wartość dla każdej z nich
# oraz spróbuj zmienić jej wartość.

class Point:
    counter = []
    def __init__(self, x=0, y=0):
        """Constructor with default attribute values"""
        self.x = x
        self.y = y

    def update(self, n):
        """Method that allows you to extend the list with element n"""
        self.counter.append(n)

p0 = Point()
p1 = Point(1,1)
p2 = Point(2,2)

for x in range(0, 6):
    p0.update(x)

# The values are the same for all objects.
print(p0.counter)
print(p1.counter)
print(str(p2.counter) + "\n")

# I can change values inside (so attributes in class are global).
p0.counter.clear()
print(p0.counter)
print(p2.counter)
p1.counter.append(10)
p1.counter.append(5)
p1.counter.append(0)
print(p2.counter)
p2.counter.sort()
print(p0.counter)