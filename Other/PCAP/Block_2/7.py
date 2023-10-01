#What is the expected output of the following code?

consts = (3.141592, 2.718282)
try:
    print(consts[2])
except Exception as exception:
    print(exception.args)
else:
    print("('success)")

# ('tuple index out of range',)
"""
Trying to access a non-extent element of a tuple raies the IndexError exception, which is a subclass of Exception.
That is why the control falls into the only "named" except branch. The exception's args tuple will carry the following text:
'tuple index out of range'.

"""