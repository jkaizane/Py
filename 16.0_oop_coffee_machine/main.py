from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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