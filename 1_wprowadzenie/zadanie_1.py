#Napisz pierwszy skrypt, w którym zadeklarujesz po dwie zmienne każdego typu, a 
#następnie wyświetl te zmienne.

name = "Alice"
last_name = "Bogdanov"

age = 18
bank_account_value = 0

velocity = 165.78
weight = 77.31

number_one = 1.5+0.5j
number_two = 5.5+1.5j

win = False
lost = True

product_list = [
     "water", "bread"
     ]

car_list = [
     "Mercedes", "BMW"
     ]

day_tuple = (
     "Monday", "Tuesday", "Wednesday",
     "Thursday", "Friday", "Saturday",
     "Sunday"
     )

gender_tuple = (
     "Man", "Woman"
     )

game_type_dictionary = {
     "MOBA": ["League of Legends", "Dota 2"],
     "FPS": "Overwatch"
     }

hero_attributes_dictionary = {
     "HP": "680", 
     "MANA": "120"
     }

print(str(type(name)) + " " + str(type(last_name)))
print("String data variables = " + name + ", " + last_name)

print(str(type(age)) + " " + str(type(bank_account_value)))
print("Int data variables = " + str(age) + ", " + str(bank_account_value))

print(str(type(velocity)) + " " + str(type(weight)))
print("Float data variables = " + str(velocity) + ", " + str(weight))

print(str(type(number_one)) + " " + str(type(number_two)))
print("Complex data variables = " + str(number_one) + ", " + str(number_two))

print(str(type(win)) + " " + str(type(lost)))
print("Boolean data variables = " + str(win) + ", " + str(lost))

print(str(type(product_list)) + " " + str(type(car_list)))
print("List data variables = " + str(product_list) + ", " + str(car_list))

print(str(type(day_tuple)) + " " + str(type(gender_tuple)))
print("Tuple data variables = " + str(day_tuple) + ", " + str(gender_tuple))

print(str(type(game_type_dictionary)) + " " + str(type(hero_attributes_dictionary)))
print("Dictionary data variables = " + str(game_type_dictionary) + ", " 
     + str(hero_attributes_dictionary))