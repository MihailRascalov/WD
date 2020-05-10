# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

births_per_year = df.groupby("Rok")["Liczba"].sum()
chart = births_per_year.plot(color="g")
chart.set_ylabel('Liczba urodzeń')
plt.title("Wykres urodzonych dzieci w latach 2000-2017")
plt.show()