"""Given the class below complete the print() method body in a way that will ensure that the get() method is properly invoked."""

class Storage:
    def __init__(Self):
        self.rack = 1

    def get(self):
        return self.rack
    
    def print(self):
        #Insert code here

#print(Storage.get(self))
"""As the function is invoked at the class level, the target object has to be passed explicitly as an argument."""

#print(self.get())
"""This also works."""