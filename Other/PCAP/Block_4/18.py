#Which of the following snippets output True to the screen?

class A:
    def __init__(self, value, = True):
        print(Value)
a = A()
"""Although the implicit constructor invocation deson't specify any arguments, the default parameter value is used and True is printed"""



class B(A):
    pass

b = B()
"""As B doesn't define its own constructor, the superclass's constructor is invoked and, in effect, True is printed to the screen."""