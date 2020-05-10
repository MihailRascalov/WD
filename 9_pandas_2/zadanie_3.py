# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w
# ostatnich 5 latach z datasetu.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

births_per_last_5_years = df[((df.Rok <= 2017) & (df.Rok >= 2013))]
births_per_last_5_years = births_per_last_5_years.groupby("Plec")["Liczba"].sum()
wykres = births_per_last_5_years.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6, 6))
plt.title("Procentowa ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach")
plt.show()