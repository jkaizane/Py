#What is the expected output of the following code?

class Aircraft:
    def start(self):
        return "default"
    
    def take_off(self):
        start()


class Fixed_Wing(Aircraft):
    pass

class Rotor_Craft(Aircraft):
    def start(self):
        return "spin"
    

fleet = [Fixed_wing(), Rotor_Craft()]
for airship in fleet:
    print(airship.start(), end =" ")

'default spin'
"""
Note that:
Fixed_wing doesn't override Aircraft's start() method, so the invocation of start() will output the following string: 'default';
The Rotor_Craft defines its own start() function, which polymorphically overrides the function of the same name defined
in the superclass, hence Rotor_Craft's start() function prints the following string: 'spin'.

In effect, the string 'default spin' appears on the screen.


"""