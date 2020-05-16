# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem
# 0.1. Dodaj etykiety i legendę do wykresu.

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 30.1, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.axis([0, 30, -1.5, 1.5])

plt.plot(x, s, label="sin(x)")
plt.plot(x, c, label="cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykresy sin(x) oraz cos(x)")
plt.legend()
plt.show()