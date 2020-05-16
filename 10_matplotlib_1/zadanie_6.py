# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w
# lekcji 8. Następnie na jednym płótnie wyświetl 3 wykresy (jeden wiersz i 3 kolumny). Dodaj
# do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w
# całym okresie. 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości
# urodzonych kobiet, druga dla mężczyzn dla każdego roku z osobna. Czyli y to ilość
# narodzonych kobiet lub mężczyzn (dwie linie), x to rok. 3 wykres – wykres słupkowy
# przedstawiający sumę urodzonych dzieci w każdym roku.

import pandas as pd
import numpy as np
import xlrd
import openpyxl
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx)

calosc = df.groupby("Plec")["Liczba"].sum()
K = calosc[0]
M = calosc[1]

etykiety = ['K', 'M']
wartosci = [K, M]

plt.subplot(1, 3, 1)
plt.bar(etykiety, wartosci, color=(1.0, 0.0, 0.0, 0.9))
plt.ylabel('Ilość narodzin')
plt.xlabel('Płeć')
plt.title("2000-2017 ilość narodzin")

plt.subplot(1, 3, 2)
wszystkie_lata = df.groupby(["Rok", "Plec"])["Liczba"].sum().reset_index()
wszystkie_lata_K = wszystkie_lata[wszystkie_lata["Plec"] == "K"].reset_index()
wszystkie_lata_M = wszystkie_lata[wszystkie_lata["Plec"] == "M"].reset_index()
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.plot(wszystkie_lata_M["Rok"], wszystkie_lata_M["Liczba"], label="chłopcy")
plt.plot(wszystkie_lata_K["Rok"], wszystkie_lata_K["Liczba"], label="dziewczynki")
plt.legend(loc="lower right")
plt.title("Poszczególne lata narodzin")

plt.subplot(1, 3, 3)
wszystkie_lata_rok = df.groupby(["Rok"])["Liczba"].sum().reset_index()
etykiety = wszystkie_lata_rok["Rok"]
wartosci = wszystkie_lata_rok["Liczba"]
plt.ylabel('Ilość narodzin')
plt.xlabel('Rok')
plt.title("Suma narodzin w poszczególnych latach")
plt.bar(etykiety, wartosci, label="Suma narodzin", color=(0.0, 1.0, 0.0, 0.9))
plt.legend()
plt.show()