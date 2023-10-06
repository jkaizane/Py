#What is the expected output of the following code?

vect = ["alpha", "bravo", "charlie"]
new_vect = map(lambda s: s[0].upper(), vect)
print(list(new_vect)[1])

#B

""""
The lambda function returns the first argument's character in upper case.
The lambda function is applied to all vect's elements (this is how the map() function works).
The list built of new_vect will contain the 'B' character inside the element indexed by 1;
This is the only output

"""