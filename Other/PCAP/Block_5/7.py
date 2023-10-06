#What is the expected output of the following code?

def f(a, b):
    return a(b)

print(f(lambda x: x and True, 1 > 0))

#True

"""
The f() functions treas its first argument as a function, and the second as its argument;
The lambda finds the Boolean conjuction of True and its argument; in short, it returns True when the argument can be
indentified as True, e.g. when it is a non-zero number;
Invoking the lambda with 1 as its argument will result in True;
This is what we'll see printed.


"""