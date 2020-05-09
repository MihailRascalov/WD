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

df = pd.read_csv('zamowienia.csv', header=0, sep=";")

# Zadanie 3.1
column = df["Sprzedawca"]
print(column.unique())

# Zadanie 3.2
max_orders = df.sort_values(by=["Utarg"], ascending=False).head(5)
max_orders.reset_index(drop=True, inplace=True)
print(max_orders)

# Zadanie 3.3
order_numer = df.groupby("Sprzedawca")["Utarg"].count().reset_index(name="Ilosc zamowien")
print(order_numer)

# Zadanie 3.4
sum_per_country = df.groupby("Kraj")["Utarg"].sum().reset_index(name="Suma zamowien")
print(sum_per_country)

# Zadanie 3.5
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
sum_for_2005_PL = df[df['Kraj']=="Polska"]
date_from = pd.Timestamp(date(2005,1,1))
date_to = pd.Timestamp(date(2005,12,31))

sum_for_2005_PL = sum_for_2005_PL[
    (sum_for_2005_PL['Data zamowienia'] > date_from ) &
    (sum_for_2005_PL['Data zamowienia'] < date_to)
]
sum_for_2005_PL.reset_index(drop=True, inplace=True)
print(sum_for_2005_PL)
to_save_2005 = sum_for_2005_PL
sum_for_2005_PL = sum_for_2005_PL.groupby("Kraj")["Utarg"].sum().reset_index(name="Suma zamowien")
print(sum_for_2005_PL)

# Zadanie 3.6
date_from = pd.Timestamp(date(2004,1,1))
date_to = pd.Timestamp(date(2004,12,31))

average_order_value = df[
    (df['Data zamowienia'] > date_from ) &
    (df['Data zamowienia'] < date_to)
]
average_order_value.reset_index(drop=True, inplace=True)
print(average_order_value)
to_save_2004 = average_order_value
average_order_value = average_order_value["Utarg"].mean()
print(average_order_value)

# Zadanie 3.7
to_save_2004.to_csv('zamówienia_2004.csv', index=False)
to_save_2005.to_csv('zamówienia_2005.csv', index=False)