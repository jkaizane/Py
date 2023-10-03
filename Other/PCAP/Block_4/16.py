#Given the code below, which of the expressions will evaluate to True?

class Alpha:
    def say(self):
        return "Alpha"
    
class Beta(Alpha):
    def say(self):
        return "beta"
    
class Gamma(Alpha):
    def say(self):
        return "gamma"
    
class Delta(Beta, Gamma):
    pass

d = Delta()
b = Beta()

Gamma in Delta.__bases__
"""Gamma is one of the direct superclasses of Delta, so it is included in the __bases__ - that's why it's True."""