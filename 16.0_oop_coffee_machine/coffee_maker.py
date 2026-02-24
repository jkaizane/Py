class CoffeeMaker:
    """Models the machine that makes the coffee"""
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
<<<<<<< HEAD
=======

>>>>>>> 22ee79565a78d20dbedd70757df181459e695126
    def report(self):
        """Prints a report of all resources."""
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
<<<<<<< HEAD
        """Returns True when order can be made, False if ingredients are insufficient"""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}.")
                can_make = False
        return can_make
    
=======
        """Returns True when order can be made, False if ingredients are insufficient."""
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry there is not enough {item}.")
                can_make = False
        return can_make

>>>>>>> 22ee79565a78d20dbedd70757df181459e695126
    def make_coffee(self, order):
        """Deducts the required ingredients from the resources."""
        for item in order.ingredients:
            self.resources[item] -= order.ingredients[item]
<<<<<<< HEAD
        print(f"Here is your {order.name} Enjoy!")
=======
        print(f"Here is your {order.name} ☕️. Enjoy!")
>>>>>>> 22ee79565a78d20dbedd70757df181459e695126
