# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek
# z całego zbioru.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

births_all_time_gender = df.groupby("Plec")["Liczba"].sum()
chart = births_all_time_gender.plot.bar()
chart.set_ylabel('Liczba urodzeń')
chart.set_xlabel('Płeć')
plt.title("Liczba urodzonych chłopców i dziewczynek w latach 2000-2017")
plt.show()