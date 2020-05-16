# Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i
# kolorów: https://matplotlib.org/api/markers_api.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

np.random.seed(19680801)

def randrange(n, vmin, vmax):
    """
    Funkcja wspomagająca może tworzyć macierz losowych liczb o
    kształcie(n, )
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

fig = plt.figure()
ax = fig.gca(projection = "3d")
n = 100

for c, m, zlow, zhigh in [( "r" , "o" , - 50 , - 25 ), ("b" , "^" , - 30 , - 5 ), ( "g" , "s" , - 5 , 20 ), ( "y" , "p" , 20 , 45 ), ( "k" , "X" , 45 , 70 )]:
    xs = randrange(n, 23 , 32 )
    ys = randrange(n, 0 , 100 )
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c =c, marker =m)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()