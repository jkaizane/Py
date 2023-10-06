#What is the expected output of the following code?

foo = [x for x in range(4)]
spam = [x for x in foo[1:-1]]
print(spam[1])

#2

"""
The first comprehension produces a list that contains 0, 1, 2, and 3;
The second uses its two cental values only: 1 and 2;
That is why spam[1] is equal to 2.


"""