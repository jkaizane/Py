#What is the expected output of the following code?

def inc(inc):
    def do(val):
        return val + inc
    
    return do

action = inc(-1)
print(action(2))

"""The action() function is a closure built with the help of inc(), which is able to get generate functions that can increment
its argument with a previously defined value. As there is the inc(-1) invocation in the snippet, action() will reduce
its argument by 1, returning 1 as the result."""