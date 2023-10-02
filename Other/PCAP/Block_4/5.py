"""Assuming that the following code has been executed successfully, indicate the expressions which evaluate to True
and don't raise exceptions."""


class Collection:
    stamps = 2

    def __init__(self, stuff):
        self.stuff = stuff

    def dispose(self):
        del self.stuff

binder = Collection(1)
binder.dispose()

len(binder.__dict__) != len(Collecton.__dict__)
"""An object's __dict__ is not the same as __dict__ of its home class. Morever, the binder object's __dict__ is empty as
the dispose() function has been executed. Hence, these two lengths cannot be equal."""

'stamps' in Collection.__dict__
"""stamps is a class variable, and it is included in the class's __dict__"""