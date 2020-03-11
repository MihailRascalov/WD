#Napisz skrypt, który generuje tabelkę z podstawowymi wartościami
#funkcji trygonometrycznych. Wskazówka => wykorzystaj listy i
#funkcje matematyczne.

import math

sin0, sin30, sin45, sin60, sin90 = 0, 1/2, math.sqrt(2)/2, math.sqrt(3)/2, 1
cos0, cos30, cos45, cos60, cos90 = 1, math.sqrt(3)/2, math.sqrt(2)/2, 1/2, 0
tg0, tg30, tg45, tg60, tg90 = 0, math.sqrt(3)/3, 1, math.sqrt(3), "doesn't exist"

list = [
        sin0, round(sin30, 2), round(sin45, 2), round(sin60, 2), sin90,
        cos0, round(cos30, 2), round(cos45, 2), round(cos60, 2), cos90,
        tg0, round(tg30, 2), tg45, round(tg60, 2), tg90
        ]

print(list)
        