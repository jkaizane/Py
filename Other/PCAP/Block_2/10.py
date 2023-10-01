#Which of the following messages will appear on the screen when the code is run?

class Failure(IndexError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "problem"
    

try:
    print("launch")
    raise Failure("ignition")
except RuntimeError as error:
    print(error)
except IndexError as error:
    print("ignore")
else: 
    print("landing")

#launch
#There's nothing in the code that can prevent this from being printed

#ignore
"""
Because Failure is derived from IndexError, exceptions of this kind will fall into the except IndexError branch,
and that is why this line appears on the screen.
"""
