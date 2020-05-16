import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('zamowienia.csv', header=0, sep=";")

sum_per_country = df.groupby("Sprzedawca")["Utarg"].sum().reset_index(name="Suma zamowien")
sprzedawcy = sum_per_country["Sprzedawca"]
sumy_zamowien = sum_per_country["Suma zamowien"]
explode = (0, 0.1, 0, 0, 0, 0, 0.15, 0.2, 0)

wedges, texts, autotexts = plt.pie(sumy_zamowien, explode=explode ,labels=sprzedawcy,
                                   autopct='%1.1f%%', textprops=dict(color="black"), shadow=True)
plt.setp(autotexts, size=14, weight="bold")
plt.title("Udział poszczególnych sprzedawców w sprzedaży")
plt.legend(title='Sprzedawcy')
plt.show()