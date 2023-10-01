"""Which of the following snippets can be used to build a new string consisting of sorted characters contained in the 'zyx
string assigned ot the letters variable?"""

letters = 'zyx'

new_string = ''.join(sorted(letters))
"""The sorted sorted() functions returns a lsit of letters sorted in alphabetical order, 
while .join() glues the characters into one string"""


tmp = list(letters)
tmp.sort()
new_string = ''.join(tmp)
"""As tmp is a list of characters taken from letters, the .sort() method sorts the list in situ, while .join() combines
the list's elements into a string."""