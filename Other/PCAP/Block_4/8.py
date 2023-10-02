#Given the code below, indicate the code line which correctly invokes the __action() method.

class BluePrint:
    __element = 1

    def __init__(self):
        self.component = 1

    def __Action(self):
        pass
product = BluePrint()

product.__BluePrint__action()
"""This is how name mangling helps you to bypass the restrictions established by the Python's privacy policy.
Using the product._BluePrint__action() syntax makes the invocation possible."""