#What is the expected output of the following code if the file named existing_text_file is a non-zero length text file located in the working directory, and the open() function invocation is successful?

try:
    f = open("existing_text_file", "rt")
    spam = f.readlines()
    print(len(spam))
    f.close()
except IOError:
    print(-1)

"""The .readlines() method tries to read the entire contents of the file and return it as a list of lines. 
This means that the length of the returned list is equal to the number of lines contained in the file."""