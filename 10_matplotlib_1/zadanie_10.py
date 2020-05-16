import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
x = np.arange(1., 21.2, 0.2)
plt.plot(1/x, x, label='f(x)=1/x')
plt.axis([0, 1, 1, 21])
plt.xlabel('x')
plt.ylabel('1/x')
plt.title("Wykres 1/x")
plt.legend()
plt.annotate('Przykladowy opis', xy=(0.2, 5), xytext=(0.4, 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             )

plt.subplot(1, 2, 2)
x = np.arange(0, 50, 0.1)
s = np.sin(x)
plt.axis([0, 30, -2, 2])
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.xlabel('x')
plt.ylabel('sin(x), cos(x)')
plt.title("Wykres sin(x) oraz wykres cos(x)")
plt.annotate('Przykładowy opis 2', xy=(12.5, 1), xytext=(10, 1.5),
             arrowprops=dict(facecolor='red', shrink=0.1),
             )
plt.legend()
plt.show()