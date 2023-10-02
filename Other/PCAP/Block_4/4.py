#What is the expected behaviour of the following code?

class Package:
    spam = ''

    def __init__(self, content):
        Package.spam += content + ";"


envelope_1 = Package("Capacitators")
envelope_2 = Package("Transistors")
print(envelope_2.spam)

#It outputs Capacitators;Transistors;
"""The spam variable is a class variable, while the class constructor appends its string argument followed by ';'
to the variable. In effect, spam will contain the string Capacitators;Transistors"""