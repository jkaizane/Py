print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = name1 + name2
lower_case_string = combined_name.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e


love_score = str(true) + str(love)
int_love_score = int(love_score)

if (int_love_score < 10) or (int_love_score > 90):
    print(f"Your score is {int_love_score}, you go together like coke and mentos.")
elif (int_love_score >= 40) and (int_love_score <= 50):
    print(f"Your score is {int_love_score}, you are alright together.")
else:
    print(f"Your score is {int_love_score}.")
