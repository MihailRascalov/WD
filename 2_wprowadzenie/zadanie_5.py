#Napisz skrypt, który pboera od użytkownika trzy
#liczby a, b i c. Sprawdza następujące warunki:
#czy a zawiera się w przedziale (0,10> oraz czy
#jednocześnie a>b lub b>c. Jeżeli warunki
#są spełnione lub nie to ma się wyswietlić odpowiedni
#komunikat na ekranie.

print("Insert three numbers")
a = input()
b = input()
c = input()
a = float(a)
b = float(b)
c = float(c)

if a > 0 and a <= 10:
    if a > b or b > c:
        print("The conditions have been met")
    else:
        print("The conditions haven't been met")
else:
    print("The conditions haven't been met")