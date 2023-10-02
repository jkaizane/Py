#What is the expected outcome of the following code?

class Economy:
    def __init__(self):
        self.econ_attr = True

class Business(Economy):
    def __init__(self):
        super().__init__()
        self.busn_attr = False

econ_a = Economy()
econ_b = Economy()
busn_a = Business()
busn_b = busn_a
print(isinstance(busn_a, Economy) and isinstance(econ_a, Business), end=" ")
print(busn_b is busn_a or econ_a is econ_b)

"""
busn_a is an instance of the Economy class as it is an object of Economy's sublass -> True;
econ_a is not an instance of the Business class as it is an object of Business's superclass -> False

True and False -> False

busn_a and busn_b actually refer to the same object, hence busn_b is busn_a evaluates to True
econ_a and econ_b refer to different objects, thus econ_a is busn_b evaluates to False;

True or False -< True


"""