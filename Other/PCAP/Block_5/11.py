#What is the expected output of the following code?

def quote(quo):

    def embed(str):
        return quo + str + quo
    
    return embed

dblq = quote('"')

print(dblq('Jane Doe'))

#"Jane Doe"

"""An example of how the closure concept is implemented """