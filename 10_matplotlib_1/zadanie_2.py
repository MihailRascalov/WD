# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie
# ekranu.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1., 20)
plt.plot(x, 1/x, "g>:", label="f(x) = 1/x")
plt.axis([1, 20, 0, 1])
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Wykres funkcji f(x) dla x [1, 20]")
plt.legend()
plt.show()