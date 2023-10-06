#What is the expected output of the following code?

def f(1):
    return 1(-3, 3)

print(f(lambda x,y: x if x > y else y))

"""The lambda function used by the code finds the greater of its two arguments. The function is passed as an argument to
f(), which invokes the lambda with two arguments: -3 and 3. In effect, 3 appears on the screen."""