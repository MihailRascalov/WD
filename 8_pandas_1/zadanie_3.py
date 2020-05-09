# Wczytaj plik /datasets/zamowieniana.csv a następnie wyświetl:

# listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# 5 najwyższych wartości zamówień
# ilość zamówień złożonych przez każdego sprzedawcę
# sumę zamówień dla każdego kraju
# sumę zamówień dla roku 2005, dla sprzedawców z Polski
# średnią kwotę zamówienia w 2004 roku,
# zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

import pandas as pd
import numpy as np
from datetime import date

# Zadanie 3.1
df = pd.read_csv('zamowienia.csv', header=0, sep=";")
# column = df["Sprzedawca"]
# print(column.unique())

# Zadanie 3.2
# print(df.sort_values(by=["Utarg"], ascending=False).head(5))

# Zadanie 3.3
# x = df.groupby("Sprzedawca").count()
# x = x.rename(columns={"Kraj": "Ilosc zamowien"})
# print(x.drop(["Data zamowienia", "idZamowienia", "Utarg"], axis=1))

# Zadanie 3.4
# y = df.groupby("Kraj")["Utarg"].sum()
# print(y)

# Zadanie 3.5
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# z = df[df['Kraj']=="Polska"]
# date_from = pd.Timestamp(date(2005,1,1))
# date_to = pd.Timestamp(date(2005,12,31))

# z = z[
    # (z['Data zamowienia'] > date_from ) &
    # (z['Data zamowienia'] < date_to)
# ]
# z.reset_index(drop=True, inplace=True)
# print(z)
# to_save_2005 = z
# z = z.groupby("Kraj")["Utarg"].sum()
# print(z)

# Zadanie 3.6
# df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
# date_from = pd.Timestamp(date(2004,1,1))
# date_to = pd.Timestamp(date(2004,12,31))

# x = df[
    # (df['Data zamowienia'] > date_from ) &
    # (df['Data zamowienia'] < date_to)
# ]
# x.reset_index(drop=True, inplace=True)
# print(x)
# to_save_2004 = x
# x = x["Utarg"].mean()
# print(x)

# Zadanie 3.7
# to_save_2004.to_csv('zamówienia_2004.csv', header=0, index=False)
# to_save_2005.to_csv('zamówienia_2005.csv', header=0, index=False)
