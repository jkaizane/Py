#What is the expected behavior of the following code?

class Tin:
    label = "Soup"

    def __init__(self, prefix):
        self.name = prefix + " " + Tin.label


can_1 = Tin("Tomato")
can_2 = Tin("Chicken")
print(can_1.label == can_2.label)

#True
"""As label is a class variable, each class object sees the same variable value, hence the code prints True."""