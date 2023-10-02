#Given the code below, indicate the code lines which correctly increment the __element variable by one.

class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __action(self):
        pass
product = BluePrint()

BluePrint._BluePrint__element += 1

"""This is an example of name mangling: using the BluePrint._BluePrint__element syntax we are able to bypass the variable's
privacy using its home class name, and to access its value."""

product._BluePrint__element +=1

"""Another example of name mangling: using the product.BluePrint__element syntax we are able to bypass the variable's
privacy using its object name, and to access its value."""