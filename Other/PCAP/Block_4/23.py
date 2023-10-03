#Given the class hierarchy presented below, indicate which of the following class declarations are legal.

class Top:
    pass

class Left(Top):
    pass

class Right(Top):
    pass


#class Bottom(Left, Top):
    pass

"""The Method Resolution Order rules are met - the declaration is correct."""


class Bottom(Left, Right):
    pass

"""The declaration follows the Method Resolution Order rules, and Python will accept this."""