#Odszukaj w dokumentacji, jakie operatory można używać w instrukcjach warunkowych.
#(np.równe, różne, mniejsze bądź równe itp.)

number_one = 30
number_two = 20

if number_one == number_two:
    print(str(number_one) + " is equal " + str(number_two))

if number_one != number_two:
    print(str(number_one) + " isn't equal " + str(number_two))

if number_one < number_two:
    print(str(number_one) + " is smaller than " + str(number_two))

if number_one <= number_two:
    print(str(number_one) + " is smaller or equal than " + str(number_two))

if number_one > number_two:
    print(str(number_one) + " is bigger than " + str(number_two))

if number_one >= number_two:
    print(str(number_one) + " is bigger or equal than " + str(number_two))

if number_one and number_two >= 30:
    print(str(number_one) + " and " + str(number_two) 
        + " are bigger or equal than " + str(20))

if number_one or number_two >= 20:
    print(str(number_one) + " or " + str(number_two) 
        + " is bigger or equal than " + str(20))

print("Available if statements operators:")
print("==, !=, <, <=, >, >=, and, or")