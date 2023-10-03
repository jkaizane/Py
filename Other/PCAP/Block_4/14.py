#Given the code below, which of the expressions will evaluate to True?

class Top;
    
    value = 3

    def say(self):
        return self.value
    
class Middle(Top):
    value = 2

class Bottom(Middle):
    def say(self):
        return -self.value
    
short = Bottom()
tall = Top()
average = Middle()


short.value == 2
"""This attribute's value has been defined at the Middle class level, short's superclass."""