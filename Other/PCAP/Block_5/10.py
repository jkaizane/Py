#What is the expected output of the following code?

vect = ["alpha", "bravo", "charlie"]
new_vect = filter(lambda s: s[-1].upper() in ["A", "O"], vect)
for x in new_vect:
    print(x[1], end="")

#lr
"""The filter() function will drop all vect's elements whose last character in uppercase is neither 'A' nor 'O'.
As both "alpha" and "bravo" meet the requirement, they will be included in the new_vecty. Later, the for loop prints the 
second character of the vector it iterates through, so lr will be printed.

"""