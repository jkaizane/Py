#What is the expected output of the following code?

plane = "Blackbird"
counter = 0 
for c in plane + 2:
    if c in ["1", "2"]:
        counter += 1
print(counter)

#The code is erroneous and cannot be run.
"""The source of problem is located in the phrase: plane + 2. You can add strings, and integers to integers, but adding
integers to strings is prohibited. Expect the TypeError exception."""