#Odszukaj w dokumentacji, jakie operatory można
#używać w instrukcjach warunkowych (np.równe, różne, mniejsze 
#bądź równe itp.)

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