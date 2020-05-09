# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):

# tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# tylko rekordy gdzie nadane imię jest takie jak Twoje
# sumę wszystkich urodzonych dzieci w całym danym okresie,
# sumę dzieci urodzonych w latach 2000-2005
# sumę urodzonych chłopców i dziewczynek,
# najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

from zadanie_1 import df

# Zadanie 2.1
# print(df[df["Liczba"]>1000])

# Zadanie 2.2
# print(df[df["Imie"]=="MICHAŁ"])

# Zadanie 2.3
# print(df["Liczba"].sum())

# Zadanie 2.4
# df_sum = df.groupby("Rok")["Liczba"].sum()
# print(df_sum.head(6).sum())

# Zadanie 2.5
# print(df.groupby("Plec")["Liczba"].sum())

# Zadanie 2.6
# x = df.loc[df.reset_index().groupby(["Rok", "Plec"])["Liczba"].idxmax()]
# x.reset_index(drop=True, inplace=True)
# print(x.drop(["Liczba", "Plec"], axis=1))

# Zadanie 2.7
# x = df.loc[df.reset_index().groupby(["Plec"])["Liczba"].idxmax()]
# x.reset_index(drop=True, inplace=True)
# print(x.drop(["Liczba", "Plec"], axis=1))
