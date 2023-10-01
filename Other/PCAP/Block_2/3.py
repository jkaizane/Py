#What is the expected outcome of the following code?

x, y = 3.0, 0.0
try:
    z = x / y
except ArithmeticError:
    z = -1
else:
    z = -2
print(z)

# -1
"""Dividing by 0.0 raises the ZeroDivisionError exception, so the control falls into the first except branch, 
which sets the z variable to -1, resulting in the else branch being bypassed. In effect, -1 is outputted to the screen."""