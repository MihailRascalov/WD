import random

random.seed()

x = random.randint(1, 1000000)

print("Serching...")
while (x != 50):
    print("Won number = " + str(x))
    x = random.randint(1, 1000000)
else:
    print("I found 50!")