# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

colors_list = ["b", "g", "r", "c", "m"]
for color_index in range(0, 5):
    fig = plt.figure( figsize =( 8 , 3 ))
    ax = fig.gca(projection = "3d")
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, shade = True, color=colors_list[color_index])
    ax.set_title("Wykres słupkowy zacieniony")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show(block=False)
    plt.pause(3)
    plt.close()