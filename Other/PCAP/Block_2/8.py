#What is the expected output of the following code?

consts = (3.141592, 2.718282)
try:
    print(consts.index(314e-2))
except Exception as exception:
    print(exception.args)
else:
    print("('success)")

# ('3.14 is not in the list',)
"""
Although 314e-2 is close to 3.141592, these two values are different, so the .index() method fails, raising the ValueError
exception. The exception's args tuple will carry the following text: '3.14 is not in list' (which is evidently true).

"""