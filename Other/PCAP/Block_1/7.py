#What is the expected output of the following code?

import math

x = -1.5
print(abs(math.floor(x) + math.ceil(x)))

#3
"""
math.floor(-1.5) == 2
math.ceil(-1.5) == -1
(-2) + (-1) == -3
abs(-3) == 3

"""