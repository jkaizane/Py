#What is the expected outcome of the following code?

x, y = 0.0, 3.0
try:
    z = x / y
except ArithmeticError:
    z = -1
else:
    z = -2
print(z)

# -2
"""Dividing by 3.0 doesn't raise any exception, so the control falls into the else branch, which sets the z variable to -2.
In effect, -2 is outputted to the screen.
"""