#Which of the following expressions evaluate to False and raise no exception?

not 'a' in 'abc'
"""not x in y is NOT THE SAME as x not in y.
not x in y is actually evaluated as (not x) in y. As not 'a' evalautes to False, the expression returns False, too."""

'123' in '1-2-3'
#False