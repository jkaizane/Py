#What is the expected output of the following code?

s = lambda x: 0 if x == 0 else 1 if x > 0 else -1

print(s(-273.15))

"""The lambda function defined in the code implements the signum function(mathematicians know it as sgn(x), which returns:)

-1 if its argument is less than zero;
0 if the argument is zero;
or 1 when the argument is greater than zero.

Hence -1 is printed.

"""