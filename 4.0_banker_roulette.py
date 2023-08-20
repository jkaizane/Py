import random

names_string = input("Give me everybody's names, separated by a comma.\n")

names = names_string.split(", ")

list_names = len(names)

random_choice = random.randint(0, list_names - 1)
person_to_pay = names[random_choice]


print(f"{person_to_pay} is going to buy the meal today!")