# Describe Problem
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")
my_function()

# Reproduce the bug
from random import randint
dice_imgs = ["1", "2", "3", "4", "5", "6"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

# Play computer and read each line

year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

# Fix the errors
age = input(int("How old are you?"))
if age > 18:
    print(f"You can drive at age {age}.")

# Print is your friend

# Use a debugger