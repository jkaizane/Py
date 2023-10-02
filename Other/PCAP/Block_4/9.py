#Given the class below, indicate a method which will correctly provide the value of the rack field?

class Storage:
    def __init__(self):
        self.rack = 1

    # Insert a method here.


stuff = Storage()
print(stuff.get())

#inserted method
def get(self):
    return self.rack