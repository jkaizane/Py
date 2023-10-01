#What is the expected outcome of the following code?

def fun(x):
    assert x >= 0
    return x ** 0.5

def mid_level (x):
    try:
        fun(x)
    except Error:
        raise

try:
    x = mid_level(-1)
except RuntimeError:
    x =-1
except:
    x = -2
print(x)

# -2

"""
1. mid_level() is invoked with the argument set to -1;
2. Assertion fails and the AssertionError exception is raised;
3. The exception is handled by the except Error: branch inside the mid_level() function; in effect the raise instruction
is executed and the AssertionError is raised again;
4. Because AssertionError is not a subclass of Runtime Error, the control falls into the default except: branch,
which sets x to -2;
5. Finally, -2 is printed to the screen.

"""