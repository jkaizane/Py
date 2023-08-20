
year = int(input("Which year do you want to check? "))


four = 4
one_hundred = 100
four_hundred = 400

if year % four != 0:
    print("Not Leap year.")
elif year % one_hundred != 0:
    print("Leap year.")
elif year % four_hundred != 0:
    print("Not Leap year.")
else:
    print("Leap year.")