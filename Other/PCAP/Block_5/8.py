#What is the expected output of the following code?

v = [1, 2, 3]

def g(a,b,m):
    return m(a,b)

print(g(1, 1, lambda x,y: v[ z:y+1 ]))

#[2]

"""
The lambda takes its two arguments and uses them as limits for the slicing the v list;
The g() function uses its third argument as a function to invoke while the first two arguments are passed to it;
The slice v[1:1] evaluates to [2]

"""