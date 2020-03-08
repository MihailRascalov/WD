#Napisz skrypt, w którym stworzysz operatory przyrostkowe dla
#operacji: +,-,*,/,**,%

number = 10
print("Initial number = " + str(number))
number += 1
print("Result = " + str(number))
number -= 2
print("Result = " + str(number))
number *= 3
print("Result = " + str(number))
number /= 4
print("Result = " + str(number))
number **= 5
print("Result = " + str(round(number, 2)))
number %= 6
print("Result = " + str(round(number, 2)))