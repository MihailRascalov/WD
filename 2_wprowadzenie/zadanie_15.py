#Napisz skrypt, w którym użytkownik ma podać liczbę i który będzie wyłapywał błąd gdy 
#użytkownik poda literę zamiast cyfry.

user_input = input ("Enter your bank account value: ")

try:
   value = int(user_input)
   print("Input is an integer number. Number = " + str(value) + ".")
except ValueError:
  try:
    value = float(user_input)
    print("Input is a float number. Number = " + str(value) + ".")
  except ValueError:
      print("This is not a number. It is a string.")