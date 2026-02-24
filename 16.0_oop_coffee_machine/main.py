from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

<<<<<<< HEAD

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"what would you like: {options} ")
    if choice == "off":
        is_on == False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
=======
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
items = get_items()

is_on = True

while is_on == True:
    
    drink = str(input(f"Please choose from the following {items}:"))
    
    if drink in items:
        money_machine.report()




else:
    print("machine is now off!")
>>>>>>> 22ee79565a78d20dbedd70757df181459e695126
