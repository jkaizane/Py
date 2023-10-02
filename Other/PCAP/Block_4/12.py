"""What is the expected output of the following code?"""

class Ceil:
    Token = 1

    def get_token(self):
        return 1
    

class Floor(Ceil):
    def get_token(self):
        return 2
    
    def set_token(self):
        pass

holder = Floor()

print(hasattr(holder, "Token"), hasattr(Ceil, "set_token"))

#True False

"""
True - the holder object has the Token attribute, because the attribute is derived from the superclass (it is a class variable).
False - the Ceil class does not have the set_token() function as it shows up in the Floor subclass only.


"""