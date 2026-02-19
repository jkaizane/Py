from oop_coffee_machine import Menu, MenuItem
import oop_coffee_machine.coffee_maker.CoffeeMaker
import oop_coffee_machine.money_machine.MoneyMachine

money_machine = MoneyMachine()

money_machine.report()

items = get_items()

drink = str(input(f"Please choose from the following {items}:"))

if drink in items:
    is_resource_sufficient(items)