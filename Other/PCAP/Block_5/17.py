#What is the expected output of the following code if there is no file named non-existing-file in the working directory/folder, and the open() function invocation is successful?

try:
    f = open("non_existing_file", "w")
    print(1, end=" ")
    s = f.readline()
    print(2, end=" ")
except IOError as error:
    print(3, end=" ")
else:
    f.close()
    print(4, end=" ")

    #1 3

    """Trying to read frm a file opened in write mode will end in disaster. An exception is raised, and the
    print(2, end=" ") invocation cannot be reached. In effect, the else branch is bypassed, too. This is why the only digits
    on the screen are 1 and 3."""