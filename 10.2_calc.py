def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { 
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the line above: ")

if symbol == "+":
    def add():
elif symbol == "-":
    def subtract():
elif symbol == "*":
    def multiply():
elif symbol == "/":
    def divide():
        
    


        

