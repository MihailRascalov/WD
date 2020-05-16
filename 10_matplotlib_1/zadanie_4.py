# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji, tak aby 
# osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30.1, 0.1)
s = np.sin(x)
s2 = np.sin(x+3.14)
plt.axis([-1.5, 31.5, -1.25, 3.25])

plt.plot(x, s+2, label="sin(x)")
plt.plot(x, s2, label="sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Wykres sin(x), sin(x)")
plt.legend(loc="center left")
plt.show()