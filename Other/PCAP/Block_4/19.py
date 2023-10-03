#What is the expected behaviour of the following snippet?

class Team:
    def show_ID(self):
        print(self.get_ID())
    
    def get_ID(self):
        return "anonymous"
    

class A(Team):
    deg get_ID(self):
    return "Alpha"

a = A()
a.show_ID()

#It outputs Alpha
"""Polymorphism and the fact that the A class has overriden the show_ID() function's definition, means that the output will
read Alpha, not anonymous."""