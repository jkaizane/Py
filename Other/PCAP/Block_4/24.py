#What is the expected output of the following code?

class Top:
    def __str__(self):
        return '1'
    

class Left(Top):
    def __str__(self):
        return '2'
    

class Right(Top):
    def __str__(self):
        return '3'
    
class Bottom(Right, Left):
    pass

object = Bottom()
print(object)

#3
"""According to the Method Resolution Order, the Bottom class will be searched through first in order to get the string
representation of the object, so the Bottom class's __str__() function will be invoked - so 3 is printed."""