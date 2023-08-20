import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#shuffles the items inside the lists

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

# selects a range from the list with the inputted number 

comb1 = letters[0:nr_letters + 1]
comb2 = symbols[0:nr_symbols + 1]
comb3 = numbers[0:nr_numbers + 1]

#converts the list into a string

str_comb1 = "".join(comb1)
str_comb2 = "".join(comb2)
str_comb3 = "".join(comb3)

# assigns each selected letter from the range to the variable

for comb in comb1:
    comb += str_comb1

for comb in comb2:
    comb += str_comb2

for comb in comb3:
    comb += str_comb3

#concatenates all variables into one

final_comb = str_comb1 + str_comb2 + str_comb3

#converts it into a list

#final_comb2 = final_comb.split()

#shuffles the list

#random.shuffle(final_comb2)



print(final_comb)