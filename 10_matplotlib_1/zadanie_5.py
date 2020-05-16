# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris) wygeneruj
# wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’, dodaj
# paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną
# z różnicy wartości poszczególnych elementów wektorów x oraz y.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm", "Species"])

x = df["SepalLengthCm"]
y = df["SepalWidthCm"]

data = {"x": x,
        "y": y,
        "c": np.random.randint(0, 50, 150),
        "s": abs(x.subtract(y))}

plt.scatter('x', 'y', c='c', s='s', data=data)
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.show()