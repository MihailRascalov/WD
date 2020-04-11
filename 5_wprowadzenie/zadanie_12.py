# Za pomocą wyrażenia generującego stwórz generator zwracający polskie nazwy miesięcy.

month_names_pl = ("Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec",
                 "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień")

months = (month for month in month_names_pl)
for x in range (0, 12):
    print(next(months))