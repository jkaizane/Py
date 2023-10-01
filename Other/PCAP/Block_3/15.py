#Which of the following can be used to find a given substring within a string?

#The .index() method
"""it is a good idea but it can also raise a ValueError when the searched substring is not found.
'Flash Gordon'.index('ash') will return 2 anyway"""

#The .rfind() method.
"""'Flash Gordon'.rfind('ash') will evaluate to 2 - the place within the strin where 'ash' starts."""