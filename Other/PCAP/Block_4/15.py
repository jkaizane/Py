#Given the code below, which of the expressions will evaluate to True?

class Alpha:
    value = "Alpha"

    def say(self):
        return self.value.lower()
    

class Beta(Alpha):
    value = "Beta"

class Gamma(Alpha):
    def say(self):
        return self.value.upper()
    
class Delta(Gamma, Beta):
    pass

d = Delta()
b = Beta()

d.say == "BETA"
"""According to Python's Method Resolution Order (MRO), say() in the d object comes from the beta class definition,
hence the comparison results in True"""

isinstance(d, Beta)
"""As d is an object of Beta's sublcass, it is an instance of Beta and the isinstance() invocation returns True"""