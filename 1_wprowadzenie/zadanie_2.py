#Stwórz skrypt kalkulator, w którym wykorzystasz wszystkie
#podstawowe działania arytmetyczne

def Multiply(x, y):
    return x*y

def Divide(x, y):
    return x/y

def Add(x, y):
    return x+y

def Subtract(x, y):
    return x-y

number_one, number_two = 50, 2
print("Multiplication result " + str(number_one) + " * " 
     + str(number_two) + " = " + str(Multiply(number_one, number_two)))
print("Division result " + str(number_one) + " / " 
     + str(number_two) + " = " + str(Divide(number_one, number_two))) 
print("Addition result " + str(number_one) + " + " 
     + str(number_two) + " = " + str(Add(number_one, number_two))) 
print("Subtraction result " + str(number_one) + " - " 
     + str(number_two) + " = " + str(Subtract(number_one, number_two)))