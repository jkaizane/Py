#What is expected output of the following code?

strng = '\''.join(("Mary", "had", "21", "sheep"))
print(strng[0:1].islower())

"""
1. '\''.join(("Mary", "had", "21", "sheep")) returns "Mary'had'21'sheep"
2. Mary'had'21'sheep"[0:1] returns "M"
3. "M".islower() returns False
"""