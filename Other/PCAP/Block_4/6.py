"""Assuming that the following code has been executed successfully, indicate the expressions which evaluate to True
and don't raise exceptions."""

class Class:
    class_var = 1

    def __init__(self):
        self.instance_var = 1

    def method(self):
        pass

object = Class()

'__dict__' in Class.__dict__

"""__dict__ is included in __dict__, just like any other component of the class."""

Class.__dict__['method'] != None
"""As class methods are included in the class's __dict__, and the method of the specified name exists,
the left side of the comparison is definitely not None"""