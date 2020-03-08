#Napisz skrypt, w którym stworzysz operatory przyrostkowe dla
#operacji: +,-,*,/,**,%

number_one = 10
number_two = 5
print("Initial number = " + str(number_one))

print(str(number_one) + " += " + str(number_two))
number_one += number_two
print("=> " + str(number_one))

print(str(number_one) + " -= " + str(number_two))
number_one -= number_two
print("=> " + str(number_one))

print(str(number_one) + " *= " + str(number_two))
number_one *= number_two
print("=> " + str(number_one))

print(str(number_one) + " /= " + str(number_two))
number_one /= number_two
print("=> " + str(number_one))

print(str(number_one) + " **= " + str(round(number_two, 2)))
number_one **= number_two
print("=> " + str(number_one))

print(str(number_one) + " %= " + str(round(number_two, 2)))
number_one %= number_two
print("=> " + str(number_one))