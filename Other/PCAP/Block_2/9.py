#Which of the following messages will appear on teh screen when code is run?

class Accident(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"
    

try:
    print("action")
    raise Accident("accident")
except Accident as accident:
    print(accident)
else:
    print("success")


#problem
"""
This message will appear on the screen as a result of the print(accident) function invocation.
As the Accident class has its __str__() function overriden in order to return the string "problem" every time,
printing this class's object will show you this text on the screen.
"""

#action
"""
This message is printed as there are no obstacles to executing the print() invocation
"""