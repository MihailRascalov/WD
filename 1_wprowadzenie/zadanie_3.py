#Napisz skrypt, w którym stworzysz operatory przyrostkowe dla operacji: +,-,*,/,**,%.

initial_number = 10
operation_number = 5

print("Initial number = " + str(initial_number))
print("Operation number = " + str(operation_number))

print(str(initial_number) + " += " + str(operation_number))
initial_number += operation_number
print("=> " + str(initial_number))

print(str(initial_number) + " -= " + str(operation_number))
initial_number -= operation_number
print("=> " + str(initial_number))

print(str(initial_number) + " *= " + str(operation_number))
initial_number *= operation_number
print("=> " + str(initial_number))

print(str(initial_number) + " /= " + str(operation_number))
initial_number /= operation_number
print("=> " + str(initial_number))

print(str(initial_number) + " **= " + str(round(operation_number, 2)))
initial_number **= operation_number
print("=> " + str(initial_number))

print(str(initial_number) + " %= " + str(round(operation_number, 2)))
initial_number %= operation_number
print("=> " + str(initial_number))